#
# spec file for package python-celerymon
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
Name:           python-celerymon
Version:        1.0.3+git.1572430376.dac5d9f
Release:        0
Summary:        Real-time monitoring of Celery workers
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/auvipy/celery-flower
Source:         celery-flower-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_py2k_bug.patch bsc#1192677 mcepl@suse.com
# Remove py2k error
Patch0:         fix_py2k_bug.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-celery
Requires:       python-tornado
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
celerymon - Real-time monitoring of Celery workers

%prep
%autosetup -p1 -n celery-flower-%{version}

find -name "*.js" -o -name "*.php" -exec sed -i 's/\r$//' {} \;
find -name '*.htm' -exec chmod -x {} \;

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/celerymon

%{python_expand \
find %{buildroot}%{$python_sitelib} \( -name '*.js' -o -name '*.php' -o -name '*.tsv' \) -exec chmod -x {} \;
%fdupes %{buildroot}%{$python_sitelib}
}

%post
%python_install_alternative celerymon

%postun
%python_uninstall_alternative celerymon

%files %{python_files}
%license LICENSE
%doc AUTHORS README
%python_alternative %{_bindir}/celerymon
%{python_sitelib}/celerymon*

%changelog
