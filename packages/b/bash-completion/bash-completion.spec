#
# spec file for package bash-completion
#
# Copyright (c) 2025 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "doc"
%define build_core 0
%define build_doc 1
%define nsuffix -doc
%else
%define build_core 1
%define build_doc 0
%endif

%global _name   bash-completion
Name:           %{_name}%{?nsuffix}
Version:        2.12.0
Release:        0
%if %{build_core}
Summary:        Programmable Completion for Bash
License:        GPL-2.0-or-later
%else
Summary:        The Documentation of Programmable Completion for Bash
License:        GPL-2.0-or-later
Provides:       bash-completion:%{_defaultdocdir}/%{_name}/AUTHORS
%endif
URL:            https://github.com/scop/bash-completion/
Source0:        https://github.com/scop/bash-completion/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        bash-completion-rpmlintrc
# PATCH-FIX-UPSTREAM bnc#717151 -- Terminal tab autocompletion error
Patch0:         %{_name}-2.4.patch
# PATCH-FIX-SUSE bnc#1012212 -- bash tab-autocompletion hangs on TAR-archiving with --create key
Patch1:         tar-completion.patch
# PATCH-FIX-SUSE boo#905348 -- tab completion with shell variable changes command line with backslash
Patch3:         FOO-dir-completion-boo905348.patch
# PATCH-FIX-SUSE
Patch4:         qdbus-qt5.patch
# PATCH-FIX-SUSE boo#889319
Patch5:         ls-completion-boo889319.patch
# PATCH-FIX-SUSE boo#940835
Patch6:         backtick-completion-boo940835.patch
# PATCH-FIX-SUSE bsc#946875
Patch7:         LVM-completion-bsc946875.patch
# PATCH-FIX-SUSE boo#940837, bsc#959299
Patch8:         respect-variables-boo940837.patch
# PATCH-FIX-SUSE boo#958462
Patch9:         rm-completion-smart-boo958462.patch
# PATCH-FIX-SUSE boo#963140
Patch10:        backticks-bsc963140.patch
# PATCH-FIX-SUSE boo#1090515
Patch11:        bash-completion-2.7-unRAR-remove.patch
# PATCH-FIX-SUSE boo#1190929
Patch13:        boo1190929-9af4afd0.patch
# PATCH-FIX-SUSE boo#1199724
Patch14:        bsc1199724-modules.patch
# PATCH-FIX-SUSE boo#1221414 -- shells/bash-completion: Bug
Patch15:        boo1221414-scp.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildArch:      noarch
%if %{build_doc}
BuildRequires:  cmark
BuildRequires:  libxslt-tools
%endif
%if %{build_core}
Requires:       bash >= 5.1.16
%endif

%description
%if %{build_doc}
This package contains the package documentation file of the
package bash-completion.
%else
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of Bash 2.04 and later.

%package devel
Summary:        The Configuration of Programmable Completion for Bash
Provides:       bash-completion:%{_datadir}/pkgconfig/bash-completion.pc

%description devel
This package contains the package configuration file of the
package bash-completion.
%endif

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
autoreconf -fiv
%configure
%if %{build_core}
%make_build
%endif
%if %{build_doc}
pushd doc
    mkdir html
    for md in *.md
    do
        cmark $md --to html > html/${md%%.md}.html
    done
popd
%endif

%install
%if %{build_core}
%make_install
# shipping in latest systemd now
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/udevadm
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/nmcli
# shipping in latest util-linux now
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/cal
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/chsh
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/dmesg
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/eject
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/hexdump
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/hwclock
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/ionice
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/look
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/mount
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/newgrp
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/renice
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/rtcwake
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/su
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/umount
# shipping in devscripts now
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/bts
# shipped as part of libsecret
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/secret-tool
# Seems to be broken (boo#1161136)
rm -vf %{buildroot}%{_datadir}/bash-completion/completions/_adb
%endif
%if %{build_doc}
pushd doc
    mkdir -p  %{buildroot}%{_defaultdocdir}/%{_name}/html
    install -m 0644 html/* %{buildroot}%{_defaultdocdir}/%{_name}/html/
popd
install -m 0644 AUTHORS %{buildroot}%{_defaultdocdir}/%{_name}/
install -m 0644 README.md  %{buildroot}%{_defaultdocdir}/%{_name}/README
%endif

%files
%if "%{flavor}" == "doc"
%dir %{_defaultdocdir}/%{_name}
%{_defaultdocdir}/%{_name}/AUTHORS
%{_defaultdocdir}/%{_name}/README
%{_defaultdocdir}/%{_name}/html/
%else
%license COPYING
%dir %{_sysconfdir}/bash_completion.d/
%{_sysconfdir}/bash_completion.d/000_bash_completion_compat.bash
%{_datadir}/bash-completion
%config %{_sysconfdir}/profile.d/bash_completion.sh

%files devel
%dir %{_datadir}/cmake
%{_datadir}/cmake/bash-completion
%{_datadir}/pkgconfig/bash-completion.pc
# TRICK: bash-completion-devel does not require bash-completion.
# It would cause failure of directory ownership check.
# Own this directory to prevent it.
%dir %{_datadir}/bash-completion
%endif

%changelog
