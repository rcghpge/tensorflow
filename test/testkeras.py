import tensorflow as tf
import time
from tensorflow.keras import datasets, layers, models

# 🚀 Check if GPU is available
print("\n✅ Available GPUs:", tf.config.list_physical_devices('GPU'))

# 🔥 Set device (GPU if available, otherwise CPU)
device = "/GPU:0" if tf.config.list_physical_devices('GPU') else "/CPU:0"

# 📂 Load CIFAR-10 dataset (10,000 samples)
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
x_train, x_test = x_train[:10000] / 255.0, x_test[:2000] / 255.0  # Normalize and reduce dataset
y_train, y_test = y_train[:10000], y_test[:2000]

# 🎯 Define CNN Model
def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# 🚀 Train on CPU
with tf.device("/CPU:0"):
    cpu_model = create_model()
    start_cpu = time.time()
    cpu_model.fit(x_train, y_train, epochs=3, batch_size=64, validation_data=(x_test, y_test), verbose=2)
    cpu_time = time.time() - start_cpu
    print(f"\n✅ CPU Training Time: {cpu_time:.2f} seconds")

# 🔥 Train on GPU (if available)
if tf.config.list_physical_devices('GPU'):
    with tf.device("/GPU:0"):
        gpu_model = create_model()
        start_gpu = time.time()
        gpu_model.fit(x_train, y_train, epochs=3, batch_size=64, validation_data=(x_test, y_test), verbose=2)
        gpu_time = time.time() - start_gpu
        print(f"\n✅ GPU Training Time: {gpu_time:.2f} seconds")
        print(f"⚡ Speedup Factor: {cpu_time / gpu_time:.2f}x (GPU vs. CPU)")
else:
    print("\n🚨 No GPU detected! Running on CPU only.")

# 📊 Final Test on GPU (if available)
print("\n🎯 Evaluating model on test set...")
test_loss, test_acc = gpu_model.evaluate(x_test, y_test, verbose=0) if tf.config.list_physical_devices('GPU') else cpu_model.evaluate(x_test, y_test, verbose=0)
print(f"\n✅ Test Accuracy: {test_acc:.4f}")

