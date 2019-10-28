#
# spec file for package python-tagpy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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
Name:           python-tagpy
Version:        2013.1
Release:        0
Summary:        Python Bindings for TagLib
License:        MIT
URL:            https://mathema.tician.de/software/tagpy
Source:         https://files.pythonhosted.org/packages/source/t/tagpy/tagpy-%{version}.tar.gz
Patch1:         python-tagpy-no_sleep.patch
Patch2:         python-tagpy-remove_ccopt.patch
Patch3:         tagpy-no-distribute-dep.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libtag-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_python-devel
%else
BuildRequires:  boost-devel
%endif
%python_subpackages

%description
TagPy is a set of Python bindings for Scott Wheeler's TagLib. It builds upon
Boost.Python, a wrapper generation library which is part of the renowned Boost
set of C++ libraries.

Just like TagLib, TagPy can:
* read and write ID3 tags of version 1 and 2, with many supported frame types
  for version 2 (in MPEG Layer 2 and MPEG Layer 3, FLAC and MPC),
* access Xiph Comments in Ogg Vorbis Files and Ogg Flac Files,
* access APE tags in Musepack and MP3 files.

All these features have their own specific interfaces, but TagLib's generic tag
reading and writing mechanism is also supported.

%prep
%setup -q -n "tagpy-%{version}"
%patch1
%patch2
%patch3 -p1

%build
%{python_expand $python configure.py \
    --python-exe="$python" \
    --prefix="%{_prefix}" \
    --taglib-inc-dir="%{_includedir}/taglib" \
    --boost-python-libname="boost_python"
}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%{python_sitearch}/_tagpy*.so
%{python_sitearch}/tagpy/
%{python_sitearch}/tagpy-%{version}-py%{python_version}.egg-info/

%changelog
