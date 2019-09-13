#
# spec file for package erlang-retest
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


Name:           erlang-retest
Version:        1.1.1+git20160312.ffef7d0
Release:        0
%define mod_ver %(echo "%{version}" | cut -d "+" -f1)
Summary:        Erlang retest library
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/rebar/retest
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        retest-%{version}.tar.bz2
Requires:       erlang >= R13B01
BuildRequires:  erlang-rebar

%description
Erlang retest library.

%package src
Summary:        Erlang retest library
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description src
Erlang retest library.

%prep
%setup -q -n retest-%{version}

%build
%__make
epmd -kill

%install
install -Dm755 retest %{buildroot}%{_bindir}/retest
for dir in include ebin src ; do
  install -d %{buildroot}%{erlang_libdir}/retest-%{mod_ver}/${dir}
  cp -r ${dir}/* %{buildroot}%{erlang_libdir}/retest-%{mod_ver}/${dir}/
done

%files
%defattr(-,root,root)
%{_bindir}/retest
%dir %{erlang_libdir}/retest-%{mod_ver}
%{erlang_libdir}/retest-%{mod_ver}/ebin
%{erlang_libdir}/retest-%{mod_ver}/include

%files src
%defattr(-,root,root)
%{erlang_libdir}/retest-%{mod_ver}/src

%changelog
