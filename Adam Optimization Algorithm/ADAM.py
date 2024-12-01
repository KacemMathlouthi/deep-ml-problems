import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    t, m0, v0 = 0, 0, 0
    for _ in range(num_iterations):
        t += 1
        g = grad(x0)
        m0 = beta1 * m0 + (1 - beta1) * g
        v0 = beta2 * v0 + (1 - beta2) * g**2
        m_hat = m0 / (1 - beta1 ** t)
        v_hat = v0 / (1 - beta2 ** t)
        x0 = x0 - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
    return x0