# sandmark-nightly
Stores nightly runs of sandmark

# How to setup nightly notebooks on an AWS machine

1. Use the AWS setup tutorial mentioned in the [TLJH documentation](https://tljh.jupyter.org/en/latest/install/amazon.html).
2. Check the `SKEL` variable in `/etc/default/useradd` to be uncommented and it should be assigned to `/etc/skel` and it should end up looking like `SKEL=/etc/skel`.
3. Start the JupyterHub server on the aws machine which is currently empty.
4. Then open the terminal and download the setup script using `wget https://raw.githubusercontent.com/shubhamkumar13/sandmark-nightly/main/scripts/setup_aws.sh`.
5. Run the script from the terminal with `bash setup_aws.sh`.

# How to run the webapp locally

```bash
$ git clone https://github.com/ocaml-bench/sandmark-nightly.git
$ cd sandmark-nightly
$ docker build -t sandmark-nightly . -f Dockerfile
$ docker run -p 8501:8501 sandmark-nightly
```
The app will be available at `http://localhost:8501`
