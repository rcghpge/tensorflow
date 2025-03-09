import tensorflow as tf
import time
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model

# Check if GPU is available
print("\nAvailable GPUs:", tf.config.list_physical_devices('GPU'))

# Set device (GPU if available, otherwise CPU)
device = "/GPU:0" if tf.config.list_physical_devices('GPU') else "/CPU:0"

# Load CIFAR-10 dataset (5K training samples, 1K test samples)
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
x_train, x_test = x_train[:5000] / 255.0, x_test[:1000] / 255.0
y_train, y_test = y_train[:5000], y_test[:1000]

# Data Augmentation
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)
datagen.fit(x_train)

# Learning Rate Scheduling
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1)

# Generate CNN Model
def generate_model(use_resnet=False):
    if use_resnet:
        base_model = ResNet50(weights="imagenet", include_top=False, input_shape=(32, 32, 3))
        x = layers.Flatten()(base_model.output)
        x = layers.Dense(128, activation="relu")(x)
        x = layers.Dense(10, activation="softmax")(x)
        model = Model(inputs=base_model.input, outputs=x)
    else:
        model = models.Sequential([
            layers.Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)),
            layers.BatchNormalization(),
            layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
            layers.BatchNormalization(),
            layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2)),

            layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
            layers.BatchNormalization(),
            layers.Conv2D(256, (3, 3), activation='relu', padding='same'),
            layers.MaxPooling2D((2, 2)),

            layers.Flatten(),
            layers.Dense(256, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(10, activation='softmax')
        ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Train on CPU
print("\nTraining on CPU...")
with tf.device("/CPU:0"):
    cpu_model = generate_model()
    start_cpu = time.time()
    cpu_model.fit(datagen.flow(x_train, y_train, batch_size=64),
                  epochs=10, validation_data=(x_test, y_test),
                  callbacks=[lr_scheduler], verbose=2)
    cpu_time = time.time() - start_cpu
    print(f"\nCPU Training Time: {cpu_time:.2f} seconds")

# Train on GPU (if available)
if tf.config.list_physical_devices('GPU'):
    print("\nTraining on GPU...")
    with tf.device("/GPU:0"):
        gpu_model = generate_model()
        start_gpu = time.time()
        gpu_model.fit(datagen.flow(x_train, y_train, batch_size=64),
                      epochs=10, validation_data=(x_test, y_test),
                      callbacks=[lr_scheduler], verbose=2)
        gpu_time = time.time() - start_gpu
        print(f"\nGPU Training Time: {gpu_time:.2f} seconds")
        print(f"Speedup Factor: {cpu_time / gpu_time:.2f}x (GPU vs. CPU)")
else:
    print("\nNo GPU detected. Running on CPU only.")

# Evaluate model on test set
print("\nEvaluating model on test set...")
test_loss, test_acc = gpu_model.evaluate(x_test, y_test, verbose=0) if tf.config.list_physical_devices('GPU') else cpu_model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest Accuracy: {test_acc:.4f}")

