#
# spec file for package nodejs-packaging
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


%define         _rpmconfigdir %{_prefix}/lib/rpm
Name:           nodejs-packaging
Version:        10.beta11
Release:        0
Summary:        Node.js Dependency generators for openSUSE
License:        MIT
Group:          Development/Languages/NodeJS
URL:            https://github.com/marguerite/nodejs-packaging
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       gcc-c++
Requires:       nodejs-devel
Requires:       npm
Requires:       ruby
Requires:       rubygem(json)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package generates Node.js Provides/Requires dependencies
automatically for nodejs module packages in openSUSE.

%package -n npkg
Summary:        The ultimate Node.js packaging toolkit for openSUSE
Group:          Development/Languages/NodeJS
Requires:       nodejs-packaging = %{version}
Requires:       ruby
Requires:       rubygem(json)
Requires:       rubygem(nokogiri)

%description -n npkg
This package provides the ultimate Node.js packaging toolkit
for openSUSE.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/npkg
mkdir -p %{buildroot}%{_rpmconfigdir}/{nodejs,fileattrs}
# 13.2's nodejs-devel package has a /etc/rpm/macros.nodejs
%if 0%{?suse_version} == 1320
mkdir -p %{buildroot}%{_sysconfdir}/rpm
install -m0644 macros.nodejs %{buildroot}%{_sysconfdir}/rpm/macros.%{name}
%else
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m0644 macros.nodejs %{buildroot}%{_rpmmacrodir}/macros.nodejs
%endif
cp -r nodejs/* %{buildroot}%{_rpmconfigdir}/nodejs
cp -r tool/* %{buildroot}%{_datadir}/npkg
cp -r scripts %{buildroot}%{_datadir}/npkg
ln -sf %{_datadir}/npkg/npkg %{buildroot}%{_bindir}/npkg
ln -sf %{_datadir}/npkg/scripts/npkg-mgmt-pkg-batchrm.rb %{buildroot}%{_bindir}/npkg-mgmt-pkg-batchrm
ln -sf %{_datadir}/npkg/scripts/npkg-mgmt-json2pkgtxt.rb %{buildroot}%{_bindir}/npkg-mgmt-json2pkgtxt
ln -sf %{_datadir}/npkg/scripts/npkg-mgmt-merge.rb %{buildroot}%{_bindir}/npkg-mgmt-merge
install -m0644 nodejs.attr %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs.attr
install -m0755 nodejs.prov %{buildroot}%{_rpmconfigdir}/nodejs.prov
install -m0755 nodejs.req %{buildroot}%{_rpmconfigdir}/nodejs.req
install -m0755 nodejs.rb %{buildroot}%{_rpmconfigdir}/nodejs.rb
install -m0755 nodejs-fixdep.rb %{buildroot}%{_rpmconfigdir}/nodejs-fixdep.rb
install -m0755 nodejs-check.rb %{buildroot}%{_rpmconfigdir}/nodejs-check.rb
install -m0755 nodejs-symlink-deps.rb %{buildroot}%{_rpmconfigdir}/nodejs-symlink-deps.rb

%files
%defattr(-,root,root)
%doc COPYING SHORTCOMINGS README.md
%if 0%{?suse_version} == 1320
%config %{_sysconfdir}/rpm/macros.%{name}
%else
%{_rpmmacrodir}/macros.nodejs
%endif
%if 0%{?suse_version} == 1110
%dir %{_rpmconfigdir}/fileattrs
%endif
%{_rpmconfigdir}/fileattrs/nodejs.attr
%{_rpmconfigdir}/nodejs.prov
%{_rpmconfigdir}/nodejs.req
%{_rpmconfigdir}/nodejs.rb
%{_rpmconfigdir}/nodejs-fixdep.rb
%{_rpmconfigdir}/nodejs-symlink-deps.rb
%{_rpmconfigdir}/nodejs-check.rb
%{_rpmconfigdir}/nodejs

%files -n npkg
%defattr(-,root,root)
%{_bindir}/npkg
%{_bindir}/npkg-mgmt-pkg-batchrm
%{_bindir}/npkg-mgmt-json2pkgtxt
%{_bindir}/npkg-mgmt-merge
%{_datadir}/npkg

%changelog
