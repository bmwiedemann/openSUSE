#
# spec file for package git-lfs
#
# Copyright (c) 2022 SUSE LLC
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


%define rb_build_ruby_abis     %{rb_default_ruby_abi}
%define rb_build_versions      %{rb_default_ruby}

%bcond_without    build_docs

Name:           git-lfs
Version:        3.3.0
Release:        0
Summary:        Git extension for versioning large files
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/git-lfs/git-lfs
Source0:        https://github.com/git-lfs/git-lfs/releases/download/v%{version}/git-lfs-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  git-core >= 1.8.2
BuildRequires:  golang-packaging
BuildRequires:  which
BuildRequires:  golang(API) >= 1.18
Requires:       git-core >= 1.8.2
Requires(post): git-core >= 1.8.2
Requires(preun):git-core >= 1.8.2
%{go_nostrip}
%if %{with build_docs}
BuildRequires:  %{rubygem asciidoctor}
%endif

%description
Git Large File Storage (LFS) replaces large files such as audio samples,
videos, datasets, and graphics with text pointers inside Git, while
storing the file contents on a remote server.

%prep
%autosetup -p1 -a 1

%build
go build -mod=vendor --buildmode=pie .
%if %{with build_docs}
%make_build man
%endif

%install
install -D -m 755 git-lfs %{buildroot}%{_bindir}/git-lfs
%if %{with build_docs}
mkdir -p -m 755 %{buildroot}%{_mandir}/man1
mkdir -p -m 755 %{buildroot}%{_mandir}/man5
install  -m 644 man/man1/*.1 %{buildroot}%{_mandir}/man1
install  -m 644 man/man5/*.5 %{buildroot}%{_mandir}/man5
%endif

%fdupes -s %{buildroot}

%{gofilelist}

%post
git lfs install --system

%preun
if [ $1 -eq 0 ] ; then
  git lfs uninstall --system
fi

%check
export GIT_LFS_TEST_DIR=$(mktemp -d)
# test/git-lfs-server-api/main.go does not compile because github.com/spf13/cobra
# cannot be found in vendor, for some reason. It's not needed for installs, so
# skip it.
export SKIPAPITESTCOMPILE=1

%{gotest} -mod=vendor

rm -rf ${GIT_LFS_TEST_DIR}

%files
%{_bindir}/git-lfs
%license LICENSE.md
%doc CHANGELOG.md CODE-OF-CONDUCT.md CONTRIBUTING.md INSTALLING.md README.md
%if %{with build_docs}
%{_mandir}/man*/*
%endif

%changelog
