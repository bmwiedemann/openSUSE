#
# spec file for package python-psdtags
#
# Copyright (c) 2026 SUSE LLC
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

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-psdtags
Version:        2026.1.29
Release:        0
Summary:        Read and write layered TIFF ImageSourceData and ImageResources tags
License:        BSD-3-Clause
URL:            https://www.cgohlke.com
Source:         https://files.pythonhosted.org/packages/source/p/psdtags/psdtags-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Psdtags is a Python library to read and write the Adobe Photoshop(r) specific
ImageResources (#34377) and ImageSourceData (#37724) TIFF tags, which contain
image resource blocks, layer and mask information found in a typical layered
TIFF file created by Photoshop.

%prep
%autosetup -p1 -n psdtags-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a  %{buildroot}%{_bindir}/psdtags
%python_expand %fdupes %{buildroot}%{$python_sitelib}


%pre
%python_libalternatives_reset_alternative psdtags

%post
%python_install_alternative psdtags

%postun
%python_uninstall_alternative psdtags

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/psdtags
%{python_sitelib}/psdtags
%{python_sitelib}/psdtags-%{version}.dist-info

%changelog
