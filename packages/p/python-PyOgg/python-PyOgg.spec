#
# spec file for package python-PyOgg
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
Name:           python-PyOgg
Version:        0.6.9a1
Release:        0
Summary:        Python bindings for Xiphorg's Ogg Vorbis, Opus and FLAC
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Zuzu-Typ/PyOgg
Source:         https://files.pythonhosted.org/packages/source/P/PyOgg/PyOgg-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libopusenc)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
# Automatically get so numbers
Recommends:     %( ls %{_libdir}/libogg.so.*.*.* | sed -r 's/.*(libogg\.so\.[0-9]*)\..*/\1/g' )
Recommends:     %( ls %{_libdir}/libopus.so.*.*.* | sed -r 's/.*(libopus\.so\.[0-9]*)\..*/\1/g' )
Recommends:     %( ls %{_libdir}/libopusenc.so.*.*.* | sed -r 's/.*(libopusenc\.so\.[0-9]*)\..*/\1/g' )
Recommends:     %( ls %{_libdir}/libopusfile.so.*.*.* | sed -r 's/.*(libopusfile\.so\.[0-9]*)\..*/\1/g' )
Recommends:     %( ls %{_libdir}/libvorbisenc.so.*.*.* | sed -r 's/.*(libvorbisenc\.so\.[0-9]*)\..*/\1/g' )
Recommends:     %( ls %{_libdir}/libvorbisfile.so.*.*.* | sed -r 's/.*(libvorbisfile\.so\.[0-9]*)\..*/\1/g' )
Recommends:     libflac
Recommends:     libvorbis
BuildArch:      noarch
%python_subpackages

%description
PyOgg provides bindings for Xiph.org's OGG Vorbis, OGG Opus and FLAC
audio file formats.

%prep
%setup -q -n PyOgg-%{version}
# wrong-file-end-of-line-encoding
sed -i 's/\r$//' README.md README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md README.rst
%license COPYING LICENSE
%{python_sitelib}/*

%changelog
