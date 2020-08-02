#
# spec file for package erlang-rebar
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           erlang-rebar
%define normal_build    ("%{name}" == "erlang-rebar")
%define testsuite_build ("%{name}" == "erlang-rebar-testsuite")
Version:        2.6.4+git20180201.b6d3094
Release:        0
%define mod_ver %(echo "%{version}" | cut -d "+" -f1)
Summary:        A sophisticated build-tool for Erlang projects that follows OTP principles
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/rebar/rebar
Source:         rebar-%{version}.tar.bz2
Source1:        macros.erlang-rebar
Source98:       %{name}.rpmlintrc
Patch2:         tdeps_update-retest.patch
Patch5:         erlc_dep_graph-timeout.patch
# PATCH-FIX-OPENSUSE -- bmwiedemann
Patch6:         reproducible.patch
BuildRequires:  erlang >= R13B01
%if 0%{?suse_version} > 1320
BuildRequires:  strip-nondeterminism
%endif
Requires:       erlang >= R13B01
Provides:       rebar = %{version}
Obsoletes:      rebar < %{version}
%if %{testsuite_build}
# for 'make test'
BuildRequires:  erlang-rebar = %{version}
BuildRequires:  erlang-reltool
BuildRequires:  erlang-retest >= 1.1.0
BuildRequires:  git
BuildRequires:  mercurial
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
%if 1%{?erlang_libdir:0}
%define erlang_libdir %{_libdir}/erlang/lib
%endif
%endif

%description
rebar is an Erlang build tool that makes it easy to compile and
test Erlang applications, port drivers and releases.

rebar is a self-contained Erlang script, so it's easy to distribute or even
embed directly in a project. Where possible, rebar uses standard Erlang/OTP
conventions for project structures, thus minimizing the amount of build
configuration work. rebar also provides dependency management, enabling
application writers to easily re-use common libraries from a variety of
locations (git, hg, etc).

%package src
Summary:        A sophisticated build-tool for Erlang projects that follows OTP principles
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description src
rebar is an Erlang build tool that makes it easy to compile and
test Erlang applications, port drivers and releases.

%prep
%setup -q -n rebar-%{version}
%patch2 -p1
%patch5 -p1
%patch6 -p1

%build
export REBAR_DEPS_PREFER_LIBS=1
make
if [ -e /usr/bin/strip-nondeterminism ] ; then
  # normalize timestamps in the zip file
  # that starts after 3 lines at offset 51 with "PK"
  zipoffs=$(perl -ne 'if(/\APK/){print $offs;exit 0} $offs+=length($_)' rebar)
  dd if=rebar of=rebar.zip bs=$zipoffs skip=1
  strip-nondeterminism rebar.zip
  dd if=rebar.zip of=rebar bs=$zipoffs seek=1 conv=notrunc
  rm rebar.zip
fi

%install
%if %{normal_build}
install -Dm755 rebar %{buildroot}%{_bindir}/rebar
# Install RPM macros:
install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.erlang-rebar
for dir in include ebin priv src ; do
  install -d %{buildroot}%{erlang_libdir}/rebar-%{mod_ver}/${dir}
  cp -r ${dir}/* %{buildroot}%{erlang_libdir}/rebar-%{mod_ver}/${dir}/
done
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
ln -s %{erlang_libdir}/rebar-%{mod_ver}/priv/shell-completion/bash/rebar %{buildroot}%{_sysconfdir}/bash_completion.d/rebar.sh
%endif

%check
%if %{testsuite_build}
# test is broken inside OBS environment due to lack of FQDN
rm -rf inttest/ct3
rm -rf inttest/ct_cover
# test is broken due to library path resolution problem
rm -rf inttest/proto_gpb
rm -rf inttest/neotoma1
# rebar is not compatible with hg 1.0.2 delivered by SLE <= 11
# these checks will thus fail -> delete them
%if 0%{?sles_version} > 0 && 0%{?sles_version} <= 11
rm -rf inttest/tdeps1
rm -rf inttest/tdeps2
%endif
# our erlang doesn't have diameter (see bnc#728667)
rm test/rebar_dia_tests.erl
%{_bindir}/rebar eunit
%{_bindir}/retest -l debug inttest
%{_bindir}/rebar xref
%endif

%if %{normal_build}
%files
%defattr(-,root,root)
%doc README.md THANKS LICENSE rebar.config.sample
%{_bindir}/rebar
%config %{_sysconfdir}/rpm/macros.erlang-rebar
%dir %{erlang_libdir}/rebar-%{mod_ver}
%{erlang_libdir}/rebar-%{mod_ver}/ebin
%{erlang_libdir}/rebar-%{mod_ver}/include
%{erlang_libdir}/rebar-%{mod_ver}/priv
%{_sysconfdir}/bash_completion.d/rebar.sh

%files src
%defattr(-,root,root)
%{erlang_libdir}/rebar-%{mod_ver}/src
%endif

%changelog
