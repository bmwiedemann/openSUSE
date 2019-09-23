#
# spec file for package python-Send2Trash
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
# test scripts missing
%define         oldpython python
Name:           python-Send2Trash
Version:        1.5.0
Release:        0
Summary:        Python library to send files to the Trash location
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/hsoft/send2trash
Source:         https://files.pythonhosted.org/packages/source/S/Send2Trash/Send2Trash-%{version}.tar.gz
Patch0:         python2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       typelib(GObject)
Requires:       typelib(Gio)
%ifpython2
Obsoletes:      %{oldpython}-send2trash < %{version}
Provides:       %{oldpython}-send2trash = %{version}
%endif
BuildArch:      noarch

%python_subpackages

%description
Send2Trash is a small package that sends files to the Trash (or
Recycle Bin) natively and on all platforms. On OS X, it uses native
FSMoveObjectToTrashSync Cocoa calls, on Windows, it uses native (and
ugly) SHFileOperation win32 calls. On other platforms, if PyGObject
and GIO are available, it will use this. Otherwise, it will fallback
to its own implementation of the trash specifications from
freedesktop.org.

%prep
%setup -q -n Send2Trash-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
