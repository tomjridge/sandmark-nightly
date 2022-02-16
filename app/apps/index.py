from sre_constants import GROUPREF_EXISTS
import streamlit as st
import os
from git import Repo

def get_repo_obj(dirpath):
    repo = Repo(dirpath)
    return repo

def curr_branch(repo):
    git = repo.git
    branch = git.branch("--show-current")
    return branch

def latest_commit(repo):
    branch = curr_branch(repo)
    commits = list(repo.iter_commits(branch))
    return commits[0].hexsha

def get_sandmark_branch_and_commit_id(curr_workdir):
    _ = os.chdir(curr_workdir)
    _ = os.chdir("..")
    sandmark = os.getcwd() + "/sandmark"
    repo = get_repo_obj(sandmark)
    branch = curr_branch(repo)
    commit = latest_commit(repo)
    return (branch, commit)

def app():
    st.title("Sandmark Nightly")
    curr_dir = os.getcwd()
    (curr_branch, curr_commit) = get_sandmark_branch_and_commit_id(curr_dir)
    _ = os.chdir(curr_dir)
    st.markdown('''
        ### What is Sandmark Nightly?
        Sandmark Nightly is a pipeline which runs the [Sandmark](https://github.com/ocaml-bench/sandmark) benchmarks 
        and uses these results to generate graphs for important metrics.

        These results help to snapshot the changes in these metrics over a period of time.

        This pipeline consists of 2 main components :

        1. The place where it actually runs the benchmarks, 
        the machines - Turing and Navajo
        2. Display the results generated by the machines on this website

        The first part is handled by a bash script for 
        [Navajo](https://github.com/ocaml-bench/sandmark-nightly/blob/main/scripts/nightly_navajo.sh)
        and [Turing](https://github.com/ocaml-bench/sandmark-nightly/blob/main/scripts/nightly_turing.sh).
        A cronjob takes care of running the scripts on their respective machines every night and pushing it to the sandmark-nightly repository

        Second part displays the [streamlit](https://streamlit.io/) app which from the info pushed to the github repo
        

        #### There are 4 different sets of benchmarks present in the nightly runs
        - Sequential Benchmarks : 
            - Variants : 
                - OCaml 5.0+trunk
                - OCaml 5.0+stable
            - Metrics :
                - Time
                - Top Heap Words
                - Max RSS (in kB)
                - Major Collections
                - Minor Collections
    
        - Parallel Benchmarks :
            - Variants :
                - OCaml 5.0+trunk
                - OCaml 5.0+stable
            - Metrics :
                - Speedup

        - Instrumented Pausetimes (sequential) : 
            The instrumented pausetimes are not updated currently
            - Past :
                - Variants :
                    - OCaml 4.12.0+stock+instrumented
                    - OCaml 4.12.0+domains+effects+instrumented
                - Metrics :
                    - Max Latency
                    - 99.9th Percentile Latency
                    - 99th Precentile Latency

        - Instrumented Pausetimes (parallel) : 
            The instrumented pausetimes are not updated currently
            - Past :
                - Variants :
                    - OCaml 4.12.0+domains+effects+instrumented
                - Metrics :
                    - Max Latency
                    - 99.9th Percentile Latency
                    - 99th Perecentile Latency
                    - Mean Latency
        ### Machines used for generating results
        - Turing :
            - Basic Hardware and Software Info :
                ```bash
                    OS: Ubuntu 20.04.3 LTS x86_64 
                    Host: Precision 7820 Tower 
                    Kernel: 5.4.0-91-generic
                    Shell: bash 5.0.17
                    CPU: Intel Xeon Gold 5120 (28) @ 2.200GHz 
                    Memory: 2271MiB / 64067MiB
                ```
            - NUMA info :
                ```bash
                    available: 2 nodes (0-1)
                    node 0 cpus: 0 1 2 3 4 5 6 7 8 9 10 11 12 13
                    node 0 size: 31815 MB
                    node 0 free: 10261 MB
                    node 1 cpus: 14 15 16 17 18 19 20 21 22 23 24 25 26 27
                    node 1 size: 32252 MB
                    node 1 free: 19489 MB
                    node distances:
                    node   0   1 
                    0:  10  21 
                    1:  21  10 
                ```
        - Navajo :
            - Basic Hardware and Software Info :
                ```bash
                    OS: Ubuntu 20.04.1 LTS x86_64 
                    Host: PowerEdge R7425 
                    Kernel: 5.4.0-92-generic 
                    Shell: sh 
                    CPU: AMD EPYC 7551 (128) @ 2.000GHz 
                    Memory: 1839MiB / 515715MiB 
                ```
            - NUMA info :
                ```bash
                    available: 2 nodes (0-1)
                    node 0 cpus: 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 102 104 106 108 110 112 114 116 118 120 122 124 126
                    node 0 size: 257715 MB
                    node 0 free: 252585 MB
                    node 1 cpus: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 101 103 105 107 109 111 113 115 117 119 121 123 125 127
                    node 1 size: 258000 MB
                    node 1 free: 247815 MB
                    node distances:
                    node   0   1 
                    0:  10  22 
                    1:  22  10 
                ```
        
        ### Disclaimer 
        This app is not performance optimized and hence rendering time might be slow so please be patient with it, Thanks :D
    ''')
    st.subheader("Sandmark info")
    curr_branch = "Current Branch = " + curr_branch
    curr_commit = "Latest Commit = " + curr_commit
    st.text(curr_branch)
    st.text(curr_commit)