#
# spec file for package password-store
#
# Copyright (c) 2021 SUSE LLC
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


Name:           password-store
Version:        1.7.4
Release:        0
Summary:        Utility to store, retrieve, generate and synchronize passwords
License:        GPL-2.0-or-later
URL:            https://zx2c4.com/projects/%{name}/
Source:         https://git.zx2c4.com/password-store/snapshot/%{name}-%{version}.tar.xz
# remove on the next release after 1.7.4
Patch0:         https://git.zx2c4.com/password-store/patch/?id=85bb62f47ac2f518bfdb36c5dfedf5938219a9b7#/default-to-xclip.patch
BuildRequires:  bash-completion
BuildRequires:  git-core
BuildRequires:  gpg2
BuildRequires:  qrencode
BuildRequires:  tree
BuildRequires:  xz
BuildRequires:  zsh
Recommends:     (xclip or wl-clipboard)
Requires:       gpg2
Requires:       qrencode
Requires:       tree >= 1.7.0
Recommends:     pwgen
Suggests:       git-core
BuildArch:      noarch
%if 0%{?suse_version} > 1320
BuildRequires:  fish
%endif

%description
With password-store, each password lives inside of a gpg encrypted file whose
filename is the title of the website or resource that requires the password.
These encrypted files may be organized into meaningful folder hierarchies,
copied from computer to computer, and, in general, manipulated using standard
command line file management utilities.

%package        dmenu
Summary:        A dmenu interface to the "pass" program
Group:          Productivity/Other
Requires:       dmenu
Requires:       password-store
Recommends:     xdotool
BuildArch:      noarch

%description    dmenu
A dmenu interface to "pass", a password manager.

%prep
%autosetup -p1
for shell_script in src/%{name}.sh contrib/dmenu/passmenu; do
    sed -i "s|#\!%{_bindir}/env bash|#\!/bin/bash|" $shell_script
done

%build

%install
%make_install FISHCOMP_PATH=%{buildroot}%{_datadir}/fish/completions WITH_ALLCOMP="yes"
install -p -D -m 0755 contrib/dmenu/passmenu %{buildroot}%{_bindir}/passmenu
# own extensions directory for pass plugins
mkdir -p %{buildroot}%{_prefix}/lib/password-store/extensions

%check
%if 0%{?suse_version} >= 1320
%make_build test
%endif

%files
%license COPYING
%doc README
%{_mandir}/man1/pass.1%{?ext_man}
%{_bindir}/pass
%if 0%{?suse_version} <= 1320
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%endif
%{_datadir}/bash-completion/completions/pass
%{_datadir}/fish/vendor_completions.d/pass.fish
%{_datadir}/zsh/site-functions/_pass
%dir %{_prefix}/lib/password-store
%dir %{_prefix}/lib/password-store/extensions

%files dmenu
%doc contrib/dmenu/README.md
%{_bindir}/passmenu

%changelog
