#
# spec file for package go-containerregistry
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
# nodebuginfo


Name:           go-containerregistry
Version:        0.17.0
Release:        0
Summary:        Container Library and tools for working with container registries
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/google/go-containerregistry
Source:         https://github.com/google/go-containerregistry/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.21
Conflicts:      distribution-registry

%description
This is a golang library for working with container registries.

%package -n crane
Summary:        CLI tool for interacting with remote images and registries
Group:          System/Management

%description -n crane
Useful tips and things you can do with crane and other standard tools.

List files in an image
crane export registry.opensuse.org/opensuse/tumbleweed - | tar -tvf - | less

Export a file from an image
crane export registry.opensuse.org/opensuse/tumbleweed -  | tar -0xf - etc/passwd

Diff two configs
diff -u <(crane config busybox:1.32 | jq) <(crane config busybox:1.33 | jq)

Diff two manifests
diff -u <(crane manifest busybox:1.32 | jq) <(crane manifest busybox:1.33 | jq)

Diff filesystem contents
diff -u \
   <(crane export gcr.io/kaniko-project/executor:v1.6.0-debug - | tar -tvf - | sort) \
   <(crane export gcr.io/kaniko-project/executor:v1.7.0-debug - | tar -tvf - | sort)

%package -n crane-bash-completion
Summary:        Bash Completion for crane
Group:          System/Shells
Requires:       bash-completion
Requires:       crane = %{version}
Supplements:    (crane and bash-completion)
BuildArch:      noarch

%description -n crane-bash-completion
Bash command line completion support for crane.

%package -n crane-fish-completion
Summary:        Fish Completion for crane
Group:          System/Shells
Requires:       crane = %{version}
Supplements:    (crane and fish)
BuildArch:      noarch

%description -n crane-fish-completion
Fish command line completion support for crane.

%package -n crane-zsh-completion
Summary:        Zsh Completion for crane
Group:          System/Shells
Requires:       crane = %{version}
Supplements:    (crane and zsh)
BuildArch:      noarch

%description -n crane-zsh-completion
zsh command line completion support for crane.

%package -n gcrane
Summary:        GCR-specific variant of crane
Group:          System/Management

%description -n gcrane
crane is a GCR-specific variant of crane that has richer output for the ls
subcommand and some basic garbage collection support.

%package -n gcrane-bash-completion
Summary:        Bash Completion for gcrane
Group:          System/Shells
Requires:       bash-completion
Requires:       gcrane = %{version}
Supplements:    (gcrane and bash-completion)
BuildArch:      noarch

%description -n gcrane-bash-completion
Bash command line completion support for gcrane.

%package -n gcrane-fish-completion
Summary:        Fish Completion for gcrane
Group:          System/Shells
Requires:       gcrane = %{version}
Supplements:    (gcrane and fish)
BuildArch:      noarch

%description -n gcrane-fish-completion
Fish command line completion support for gcrane.

%package -n gcrane-zsh-completion
Summary:        Zsh Completion for gcrane
Group:          System/Shells
Requires:       gcrane = %{version}
Supplements:    (gcrane and zsh)
BuildArch:      noarch

%description -n gcrane-zsh-completion
zsh command line completion support for gcrane.

%prep
%setup -qa1
%autopatch -p1

%build
for i in crane gcrane registry; do
    go build -mod=vendor -buildmode=pie -trimpath ./cmd/$i
done

%install
find -name crane
for bin in crane gcrane registry; do
    install $bin -D %{buildroot}/%{_bindir}/$bin
done
# "only one tool per thing" SLE15 policy conflicts
%if 0%{?suse_version} && %{?suse_version} < 1550
rm -v %{buildroot}/%{_bindir}/registry
%endif

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/crane completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/crane

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/crane completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/crane.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/crane completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_crane

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
%{buildroot}/%{_bindir}/gcrane completion bash > %{buildroot}%{_datarootdir}/bash-completion/completions/gcrane

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
%{buildroot}/%{_bindir}/gcrane completion fish > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/gcrane.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh_completion.d/
%{buildroot}/%{_bindir}/gcrane completion zsh > %{buildroot}%{_datarootdir}/zsh_completion.d/_gcrane

%if %{?suse_version} > 1500
%files
%license LICENSE
%doc README.md
%{_bindir}/registry
%endif

%files -n crane
%license LICENSE
%{_bindir}/crane

%files -n crane-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/crane

%files -n crane-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/crane.fish

%files -n crane-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_crane

%files -n gcrane
%license LICENSE
%{_bindir}/gcrane

%files -n gcrane-bash-completion
%dir %{_datarootdir}/bash-completion/completions/
%{_datarootdir}/bash-completion/completions/gcrane

%files -n gcrane-fish-completion
%dir %{_datarootdir}/fish
%dir %{_datarootdir}/fish/vendor_completions.d
%{_datarootdir}/fish/vendor_completions.d/gcrane.fish

%files -n gcrane-zsh-completion
%defattr(-,root,root)
%dir %{_datarootdir}/zsh_completion.d/
%{_datarootdir}/zsh_completion.d/_gcrane

%changelog
