#
# spec file for package python-hug
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define skip_python36 1
# Tag/Release for 2.6.1 is missing on GitHub: https://github.com/hugapi/hug/issues/854
%define revision 9758507d5a0dbe9926e463b133ec9c5f44298b15
Name:           python-hug
Version:        2.6.1
Release:        0
Summary:        A Python framework for developing APIs
License:        MIT
Group:          Development/Languages/Python
URL:            https://www.hug.rest
# pypi does not contain tests
#Source:         https://files.pythonhosted.org/packages/source/h/hug/hug-%%{version}.tar.gz
Source:         https://github.com/hugapi/hug/archive/%{revision}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-falcon
Requires:       python-requests
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module falcon}
BuildRequires:  %{python_module marshmallow >= 3.0.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
The hug library helps to create Python APIs for multiple interfaces.

%prep
%setup -q -n hug-%{revision}
# https://github.com/hugapi/hug/issues/895
sed -i 's:pytest-runner:pytest:' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/hug

%check
# exclude tests failing most probably due to different library versions (hug uses falcon==2.0.0
%pytest -k 'not (test_transform or test_hug_post or test_marshmallow_schema or test_marshmallow_custom_context or test_validate_route_args_negative_case or test_request or test_datagram_reques or test_exception or test_raise_on_invalid or test_versioning or test_marshmallow3_support or test_exceptions or test_exception_excludes or test_current_api or test_routing_class_based_method_view_with_sub_routing)'

%post
%python_install_alternative hug

%postun
%python_uninstall_alternative hug

%files %{python_files}
%doc ARCHITECTURE.md CHANGELOG.md FAQ.md README.md documentation/
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/hug

%changelog
