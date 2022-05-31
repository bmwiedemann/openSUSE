#
# spec file for package python-azure-media-videoanalyzer-edge
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-media-videoanalyzer-edge
Version:        1.0.0b4
Release:        0
Summary:        Microsoft Azure Video Analyzer Edge SDK Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-media-videoanalyzer-edge/azure-media-videoanalyzer-edge-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-media-nspkg >= 1.0.0}
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core < 2.0.0
Requires:       python-azure-core >= 1.2.2
Requires:       python-azure-media-nspkg >= 1.0.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-msrest >= 0.6.21
Conflicts:      python-azure-sdk <= 2.0.0

BuildArch:      noarch

%python_subpackages

%description
Azure Video Analyzer provides a platform to build intelligent video applications that span the edge and
the cloud. The platform offers the capability to capture, record, and analyze live video along with
publishing the results, video and video analytics, to Azure services in the cloud or the edge. It is
designed to be an extensible platform, enabling you to connect different video analysis edge modules
(such as Cognitive services containers, custom edge modules built by you with open-source machine
 learning models or custom models trained with your own data) to it and use them to analyze live video
without worrying about the complexity of building and running a live video pipeline.

Use the client library for Video Analyzer Edge to:

* Simplify interactions with the Microsoft Azure IoT SDKs
* Programmatically construct pipeline topologies and live pipelines

%prep
%setup -q -n azure-media-videoanalyzer-edge-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-media-videoanalyzer-edge-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/media/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/media/__pycache__
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/media/videoanalyzeredge
%{python_sitelib}/azure_media_videoanalyzer_edge-*.egg-info

%changelog
