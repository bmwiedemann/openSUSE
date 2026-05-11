#
# spec file for package python-google-cloud-aiplatform
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


%{?sle15_python_module_pythons}
Name:           python-google-cloud-aiplatform
Version:        1.147.0
Release:        0
Summary:        Vertex AI API client library
License:        Apache-2.0
URL:            https://github.com/googleapis/python-aiplatform
Source:         https://files.pythonhosted.org/packages/source/g/google-cloud-aiplatform/google_cloud_aiplatform-%{version}.tar.gz
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module docstring_parser >= 0.15}
BuildRequires:  %{python_module google-api-core >= 2.10.0}
BuildRequires:  %{python_module google-auth >= 2.14.1}
BuildRequires:  %{python_module google-cloud-bigquery >= 1.15.0}
BuildRequires:  %{python_module google-cloud-resource-manager >= 1.3.3}
BuildRequires:  %{python_module google-cloud-storage >= 1.32.0}
BuildRequires:  %{python_module google-genai >= 0.1.0}
BuildRequires:  %{python_module packaging >= 14.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proto-plus >= 1.22.0}
BuildRequires:  %{python_module protobuf >= 3.19.5}
BuildRequires:  %{python_module pydantic >= 1.9.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 4.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docstring_parser >= 0.15
Requires:       python-google-api-core >= 2.10.0
Requires:       python-google-auth >= 2.14.1
Requires:       python-google-cloud-bigquery >= 1.15.0
Requires:       python-google-cloud-resource-manager >= 1.3.3
Requires:       python-google-cloud-storage >= 1.32.0
Requires:       python-google-genai >= 0.1.0
Requires:       python-packaging >= 14.3
Requires:       python-proto-plus >= 1.22.0
Requires:       python-protobuf >= 3.19.5
Requires:       python-pydantic >= 1.9.0
Requires:       python-typing-extensions >= 4.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Vertex AI API client library.

%prep
%autosetup -n google_cloud_aiplatform-%{version}

%build
export SETUPTOOLS_DISABLE_NAMESPACE_PTH=1
%pyproject_wheel

%install
export SETUPTOOLS_DISABLE_NAMESPACE_PTH=1
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/tb-gcp-uploader
%python_compileall
%python_expand find %{buildroot}%{$python_sitelib} -name "*.py" -exec touch -h -d "$(echo $SOURCE_DATE_EPOCH_MTIME | grep -q '^[0-9]\+$' && echo @)$SOURCE_DATE_EPOCH_MTIME" {} +
%python_expand find %{buildroot}%{$python_sitelib} -name "*.pyc" -delete
%python_expand find %{buildroot}%{$python_sitelib} -name "*.pth" -delete
%python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# working path file
#cat >%{python_sitelib}/google_cloud_aiplatform-nspkg.pth <<EOF
# import sys, types, os, pkgutil; m = sys.modules.setdefault('google', types.ModuleType('google')); m.__dict__.setdefault('__path__', []); m.__path__ = pkgutil.extend_path(m.__path__, 'google')
#import sys, types, os, pkgutil; m = sys.modules.setdefault('google.cloud', types.ModuleType('google.cloud')); m.__dict__.setdefault('__path__', []); m.__path__ = pkgutil.extend_path(m.__path__, 'google.cloud'); setattr(sys.modules['google'], 'cloud', m)
#EOF
%post
%python_install_alternative tb-gcp-uploader

%postun
%python_uninstall_alternative tb-gcp-uploader

%files %{python_files}
%python_alternative %{_bindir}/tb-gcp-uploader
#%%{python_sitelib}/google_cloud_aiplatform-*nspkg.pth
%{python_sitelib}/vertex_ray/
%doc README.rst
%license LICENSE
%{python_sitelib}/google/cloud/aiplatform*
%{python_sitelib}/google_cloud_aiplatform-%{version}.dist-info
%{python_sitelib}/vertexai*

%changelog
