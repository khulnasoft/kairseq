# Creating a New Release

In order to create a new release:

1. Navigate to the [Kairseq Workflows](https://github.com/khulnasoft/kairseq/actions) and find the one named _Kairseq Release_. 

2. Under _Run Workflow_ choose the branch `main` and for _Release Type_ enter either `major`, `minor`, or `patch`.  

3. A branch named `$new_version-release` will be created where the `version.txt` file is updated. Merge those changes into `main`.

4. Make sure that a [new PYPI package](https://pypi.org/project/kairseq/) has been uploaded.

5. Make sure that a [new github release](https://github.com/khulnasoft/kairseq/releases) has been created.
