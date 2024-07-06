import tensorflow as tf
import tensorflow_probability as tfp

# Define the target distribution (2D Gaussian)
def target_log_prob(x, y):
    return -0.5 * (x**2 + y**2)

# Initialize the HMC transition kernel
num_results = 1000
num_burnin_steps = 500

hmc = tfp.mcmc.HamiltonianMonteCarlo(
    target_log_prob_fn=lambda x, y: target_log_prob(x, y),
    num_leapfrog_steps=3,
    step_size=0.1
)

# Define the trace function to record the state and kernel results
@tf.function
def run_chain(initial_state, kernel, num_results, num_burnin_steps):
    return tfp.mcmc.sample_chain(
        num_results=num_results,
        num_burnin_steps=num_burnin_steps,
        current_state=initial_state,
        kernel=kernel,
        trace_fn=lambda _, pkr: pkr
    )

# Run the MCMC chain
initial_state = [tf.zeros([]), tf.zeros([])]
samples, kernel_results = run_chain(initial_state, hmc, num_results, num_burnin_steps)

# Extract the samples and log
samples_ = [s.numpy() for s in samples]
samples_x, samples_y = samples_

print("Acceptance rate: ", kernel_results.is_accepted.numpy().mean())
print("Mean of x: ", samples_x.mean())
print("Mean of y: ", samples_y.mean())
