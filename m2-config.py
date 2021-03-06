from funcx_endpoint.endpoint.utils.config import Config
from funcx_endpoint.executors import HighThroughputExecutor
from parsl.addresses import address_by_hostname
from parsl.launchers import SrunLauncher
from parsl.providers import SlurmProvider

# PLEASE UPDATE user_opts BEFORE USE
user_opts = {
    "m2": {
        "worker_init": ". ~/m2-funcx-minimal-example/setup_m2_funcx_env.sh",
    }
}

# http://faculty.smu.edu/csc/documentation/slurm.html#maneframe-ii-s-slurm-partitions-queues
config = Config(
    executors=[
        HighThroughputExecutor(
            label="M2_CPU",
            address=address_by_hostname(),
            provider=SlurmProvider(
                "htc",  # Partition / QOS
                nodes_per_block=1,
                max_blocks=1,
                init_blocks=1,
                # string to prepend to #SBATCH blocks in the submit
                # script to the scheduler eg: '#SBATCH --constraint=knl,quad,cache'
                # scheduler_options=user_opts["m2"]["scheduler_options"],
                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init=user_opts["m2"]["worker_init"],
                launcher=SrunLauncher(),
                walltime="00:10:00",
                # increase the command timeouts
                # cmd_timeout=120,
                cmd_timeout=300,
            ),
            heartbeat_threshold=300,
        ),
    ],
    heartbeat_threshold=300,
)
