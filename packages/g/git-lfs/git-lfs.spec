#
# spec file for package git-lfs
#
# Copyright (c) 2020 SUSE LLC
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

Name:           git-lfs
Version:        2.10.0
Release:        0
Summary:        Git extension for versioning large files
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://git-lfs.github.com/
Source0:        %{name}-v%{version}.tar.gz
Source1:        README.packaging
Patch0:         Makefile_path.patch
%if 0%{?suse_version} >= 1550 || (0%{?suse_version} >= 1500 && 0%{?is_opensuse})
BuildRequires:  %{rubygem ronn}
%endif
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  git-core >= 1.8.2
BuildRequires:  go1.14
BuildRequires:  golang-packaging
BuildRequires:  which
Requires:       git-core >= 1.8.2
Requires(post): git-core >= 1.8.2
Requires(preun): git-core >= 1.8.2
%{go_nostrip}
%{go_provides}

%description
Git Large File Storage (LFS) replaces large files such as audio samples,
videos, datasets, and graphics with text pointers inside Git, while
storing the file contents on a remote server.

%prep
%autosetup -p1

%build
%{goprep} github.com/git-lfs/git-lfs
%{gobuild}
%if 0%{?suse_version} >= 1550 || (0%{?suse_version} >= 1500 && 0%{?is_opensuse})
%make_build man
%endif

%install
%{goinstall}
%{gosrc}
%if 0%{?suse_version} >= 1550 || (0%{?suse_version} >= 1500 && 0%{?is_opensuse})
mkdir -p -m 755 %{buildroot}%{_mandir}/man1
mkdir -p -m 755 %{buildroot}%{_mandir}/man5
install -D -m 644 man/*.1 %{buildroot}%{_mandir}/man1
install -D -m 644 man/*.5 %{buildroot}%{_mandir}/man5
%endif

%fdupes -s %{buildroot}

%{gofilelist}

%post
git lfs install --system

%preun
git lfs uninstall

%check
export GIT_LFS_TEST_DIR=$(mktemp -d)
# test/git-lfs-server-api/main.go does not compile because github.com/spf13/cobra
# cannot be found in vendor, for some reason. It's not needed for installs, so
# skip it.
export SKIPAPITESTCOMPILE=1

%{gotest} github.com/git-lfs/git-lfs

rm -rf ${GIT_LFS_TEST_DIR}

%files -f file.lst
%{_bindir}/git-lfs
%license LICENSE.md
%doc README.md
%if 0%{?suse_version} >= 1550 || (0%{?suse_version} >= 1500 && 0%{?is_opensuse})
%{_mandir}/man*/*
%endif

%changelog
