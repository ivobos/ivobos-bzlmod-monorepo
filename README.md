
# Install bazel via bazelisk
on mac 
```
brew install bazelisk
```

# Clone repo and run on command line



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
