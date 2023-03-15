#
# spec file for package barrel
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


Name:           barrel
Version:        0.2.0
Release:        0
Summary:        Tool for storage management
License:        GPL-2.0-only
Group:          System/Packages
URL:            https://github.com/openSUSE/barrel
Source:         barrel-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libstorage-ng-devel >= 4.5.78
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  readline-devel

Requires:       libstorage-ng1 >= 4.5.78
Recommends:     %{name}-lang
Recommends:     logrotate
%if 0%{?fedora_version}
BuildRequires:  boost-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  json-c-devel
%else
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libjson-c-devel
%endif

%description
barrel is a command line tool for storage management.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"

autoreconf -fvi
%configure \
    --docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check VERBOSE=1

%install
%make_install

%fdupes -s %{buildroot}

%find_lang barrel

%files
%defattr(-,root,root)
%{_sbindir}/barrel
%dir %{_sysconfdir}/barrel
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_mandir}/*/barrel.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/barrel
%license %{_docdir}/%{name}/LICENSE

%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%files lang -f barrel.lang

%changelog
