
# nix setup
TODO: update readme to use nix flake

# Install bazel via bazelisk
on mac , also install buildifier for formatting BUILD files
```
brew install bazelisk
brew install buildifier
```

# IntelliJ integration
Make sure you have Bazel For IntelliJ plugin installed.
Clone repo and run intelliJ
```bash
git clone https://github.com/ivobos/ivobos-bazel-monorepo.git
idea ivobos-bazel-monorepo
```

Include all files in project by editing .ijwb/.bazelproject as per below and running Bazel>Sync>SyncWithBuildFiles
```
directories: 
  .
```

# build
```shell
bazel build //...
```

# test
```shell
bazel test //...
```

# run python app
```shell
bazel run projects/my-python-app/...
```

# run go app
```shell
bazel run projects/go_web
```
and visit localhost:8000 in your browser

# go build files
go build files are managed by  https://github.com/bazelbuild/bazel-gazelle
to update the BUILD files run 
```shell
bazel run //:gazelle
```