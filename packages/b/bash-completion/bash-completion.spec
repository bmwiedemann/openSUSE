#
# spec file for package bash-completion
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%bcond_without  debug

%if "%{flavor}" == "doc"
%define build_core 0
%define build_doc 1
%define nsuffix -doc
%else
%define build_core 1
%define build_doc 0
%endif
%bcond_with     checks

%global _name   bash-completion
Name:           %{_name}%{?nsuffix}
Version:        2.18.0
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
# PATCH-FIX-SUSE boo#905348 -- tab completion with shell variable changes command line with backslash
# PATCH-FIX-SUSE boo#940835
# PATCH-FIX-SUSE boo#963140
# PATCH-FIX-SUSE boo#940837, bsc#959299
Patch3:         dollar-completion-boo905348-boo940835-boo963140-boo940837.patch
# PATCH-FIX-SUSE
Patch4:         qdbus-qt5.patch
# PATCH-FIX-SUSE boo#889319
Patch5:         ls-completion-boo889319.patch
# PATCH-FIX-SUSE bsc#946875
Patch7:         LVM-completion-bsc946875.patch
# PATCH-FIX-SUSE boo#958462
Patch9:         rm-completion-smart-boo958462.patch
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
%else
%if %{with checks}
BuildRequires:  procps
BuildRequires:  psmisc
BuildRequires:  python3-base
BuildRequires:  python3-pexpect
BuildRequires:  python3-pytest
%endif
%endif
%if %{build_core}
BuildRequires:  bash
BuildRequires:  bash-sh
Requires:       bash
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
%if %{without debug}
%autosetup -p1 -n %{_name}-%{version}
%else
%setup -q -n %{_name}-%{version}
typeset -i i=0
for p_file in %{patches}; do
    : $((i++))
    echo "Apply patch $p_file with suffix .p$i ..."
    %{__patch} -p1 -b -z .p${i} --fuzz=%{_default_patch_fuzz} %{_default_patch_flags} < "$p_file"
done
%endif

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
fallback=""
remove=""
# shipping in latest systemd now
fallback="$fallback nmcli udevadm"
# shipping in latest util-linux now
fallback="$fallback cal chsh dmesg eject hexdump hwclock ionice look mount newgrp renice rtcwake su umount"
# shipping in devscripts now
fallback="$fallback bts"
# shipped as part of libsecret
fallback="$fallback secret-tool"
# Seems to be broken (boo#1161136)
remove="$remove adb"
# shipped as part of kmod
fallback="$fallback insmod insmod.static modinfo modprobe rmmod"
# shipped as part of patchutils
fallback="$fallback interdiff"
# shipped as part of tmux
fallback="$fallback tmux"

for i in $remove; do
	rm -fv "%{buildroot}%{_datadir}/bash-completion/completions-fallback/${i}.bash"
	rm -fv "%{buildroot}%{_datadir}/bash-completion/completions-core/${i}.bash"
done
for i in $fallback; do
	test -e "%{buildroot}%{_datadir}/bash-completion/completions-core/${i}.bash" || continue
	mv -fv "%{buildroot}%{_datadir}/bash-completion/completions-core/${i}.bash" \
	       "%{buildroot}%{_datadir}/bash-completion/completions-fallback/${i}.bash"
done
unset i remove fallback
%endif
%if %{build_doc}
pushd doc
    mkdir -p  %{buildroot}%{_defaultdocdir}/%{_name}/html
    install -m 0644 html/* %{buildroot}%{_defaultdocdir}/%{_name}/html/
popd
install -m 0644 AUTHORS %{buildroot}%{_defaultdocdir}/%{_name}/
install -m 0644 README.md  %{buildroot}%{_defaultdocdir}/%{_name}/README
%endif

%if ! %{build_doc}
%if %{with checks}
%check
make check
export NETWORK=none
export PYTEST_ADDOPTS="-v -k 'not test_rpm and not test_remote_path_with and not test_remote_path_ending and not test_rsync and not test_unit_compgen' \
  --deselect=t/test_curl.py::TestCurl::test_interface_ipv6 \
  --deselect=t/test_ifstat.py::TestIfstat::test_2 \
  --deselect=t/test_iperf.py::TestIperf::test_2 \
  --deselect=t/test_iperf3.py::TestIperf3::test_2 \
  --deselect=t/test_nethogs.py::TestNethogs::test_1 \
  --deselect=t/test_nload.py::TestNload::test_basic \
  --deselect=t/test_service.py::TestService::test_1 \
  --deselect=t/test_wget.py::TestWget::test_3"
make installcheck DESTDIR=%{buildroot}
%endif
%endif

%files
%if "%{flavor}" == "doc"
%dir %{_defaultdocdir}/%{_name}
%{_defaultdocdir}/%{_name}/AUTHORS
%{_defaultdocdir}/%{_name}/README
%{_defaultdocdir}/%{_name}/html/
%else
%license COPYING
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
