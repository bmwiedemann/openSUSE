#
# spec file for package python
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


# Define just "test" as a package in _multibuild file to distinguish test
# instructions here
%if "@BUILD_FLAVOR@" == ""
%define _test 0
%define name_ext %nil
%else
%define _test 1
%define name_ext -test
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         short_name openqa_review
%define         binaries openqa-review openqa-review-daily-email openqa-review-sles-ha tumblesle-release openqa-review-functional_yast_concise
%define         oldpython python
Name:           python-%{short_name}%{?name_ext}
Version:        1.19.0
Release:        0
Summary:        A review helper script for openQA
License:        MIT
Group:          Development/Languages/Python
Source:         python-%{short_name}-%{version}.tar.xz
URL:            https://github.com/okurz/%{short_name}
BuildRequires:  python-rpm-macros
%if 0%{?_test}
BuildRequires:  python3-%{short_name} == %{version}
%else
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# workaround because of python-configparser not providing the '__init__.py'
# file within site-packages/backports
%if "%{python_flavor}" == "python2"
Requires:       python-backports.ssl_match_hostname
Requires:       python-configparser
%endif
Requires:       python-PyYAML
Requires:       python-beautifulsoup4
Requires:       python-certifi
Requires:       python-future
Requires:       python-humanfriendly
Requires:       python-pika
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-sortedcontainers
Requires(post): update-alternatives
Requires(preun): update-alternatives
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%ifpython2
Obsoletes:      %{oldpython}-%{short_name} < %{version}
%endif

%if 0%{?_test}
%else
%python_subpackages
%endif

%description
A review helper script for openQA. For more details look into the README file.

%prep
%if 0%{?_test}
# workaround to prevent post/install failing assuming this file for whatever
# reason
touch %{_sourcedir}/%{short_name}
%else
%setup -q
# delete shebang of files not in executable path
find %{short_name}/ -name '*.py' -print0 | xargs -0 sed -i '1s/#!.*$//'
%endif

%build
%if 0%{?_test}
openqa-review --help
tumblesle-release --help
%else
%python_build
%endif

%install
%if 0%{?_test}
# disable debug packages in package test to prevent error about missing files
%define debug_package %{nil}
%else
%python_install
rm %{buildroot}/%{python_sitelib}/version.*

for i in %{binaries}; do
    %python_clone -a %{buildroot}%{_bindir}/$i
done
%fdupes %{buildroot}%{_prefix}

%post
%{python_install_alternative %{binaries}}

%preun
%python_uninstall_alternative openqa-review

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{python_sitelib}
%python_alternative %{_bindir}/openqa-review
%python_alternative %{_bindir}/openqa-review-sles-ha
%python_alternative %{_bindir}/openqa-review-daily-email
%python_alternative %{_bindir}/openqa-review-functional_yast_concise
%python_alternative %{_bindir}/tumblesle-release

%endif

%changelog
