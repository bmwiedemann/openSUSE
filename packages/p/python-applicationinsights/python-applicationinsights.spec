#
# spec file for package python-applicationinsights
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-applicationinsights
Version:        0.11.10
Release:        0
Summary:        Microsoft Application Insights for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/applicationinsights/applicationinsights-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-applicationinsights <= 0.11.10
%endif
BuildArch:      noarch

%python_subpackages

%description
This project extends the Application Insights API surface to support Python.

Application Insights is a service that allows developers to keep their
application available, performing and succeeding. This Python module will
allow you to send telemetry of various kinds (event, trace, exception, etc.)
to the Application Insights service where they can be visualized in the
Azure Portal.

%prep
%setup -q -n applicationinsights-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python_sitelib}/applicationinsights
%{python_sitelib}/applicationinsights-*.dist-info

%changelog
