# Minimal example of funcX on M2

## Minimal Example

1. Clone this repo to your `$HOME` directory (for PATH consistency in example)
2. Create and activate the Conda virtual environment

```console
$ . create_m2_funcx_env.sh
```
3. On the M2 login node create the `funcx-endpoint`

```console
$ funcx-endpoint configure pyhf
```

and open the link to authenticate (this will require a Globus account).

4. Then copy the example `funcx` config into place for `funcx`

```console
$ cp m2-config.py ~/.funcx/pyhf/config.py
```

5. Then startup the endpoint

```console
$ funcx-endpoint start pyhf && funcx-endpoint list
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:173 [INFO]  Starting endpoint with uuid: 12345678-abcd-abcd-abcd-123456789101
YYYY-MM-DD HH:MM:SS endpoint.endpoint_manager:238 [INFO]  Launching endpoint daemon process
+---------------+---------+--------------------------------------+
| Endpoint Name | Status  |             Endpoint ID              |
+===============+=========+======================================+
| pyhf          | Running | 12345678-abcd-abcd-abcd-123456789101 |
+---------------+---------+--------------------------------------+
```

6. Copy the Endpoint ID file to wherever you're going to submit from

```console
$ funcx-endpoint list | grep pyhf | awk '{print $(NF-1)}' > endpoint_id.txt
# From the machine to be used at submit time
# $ scp M2:~/PATH-TO-WHERE-THIS-REPO-CLONED/endpoint_id.txt .
# $ echo "endpoint_id.txt" >> .gitignore
```

7. From the submission machine, make sure that you have the same Python virtual environment setup. So enter into a Python virtual environment and then

```console
$ python -m pip install -r core-requirements.txt
```

or make the same environment with Conda.

8. Then once you're sure that on M2 the `funcx-endpoint` is running and from the submission machine `endpoint_id.txt` is correct run the test job of 5 signal patches

```console
$ time python fit_analysis.py -c config/1Lbb.json -b numpy
```

9. On M2 you'll probably want to try to monitor how things are going with `funcx-endpoint list && squeue -u $USER`.


## Observed behavior

The endpoint submits the relevant job to M2, but it hangs in the queue due to resources on the `htc` queue.
