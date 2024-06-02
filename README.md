
# nix setup
## Install nix 
from https://nixos.org/download/

## Install direnv and configure
```
brew install direnv
```
Hook direnv into shells as per https://direnv.net/docs/hook.html

Enable flake
```
sudo vi /etc/nix/nix.conf
```
Add following:
```
experimental-features = flakes nix-command
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

# run C++ app
```
bazel run projects/hello_cc:hello-world
```
