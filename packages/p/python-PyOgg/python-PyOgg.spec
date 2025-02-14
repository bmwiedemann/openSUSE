#
# spec file for package python-PyOgg
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-PyOgg
Version:        0.6.14a1
Release:        0
Summary:        Python bindings for Xiphorg's Ogg Vorbis, Opus and FLAC
License:        BSD-3-Clause
URL:            https://github.com/Zuzu-Typ/PyOgg
Source:         https://files.pythonhosted.org/packages/source/P/PyOgg/PyOgg-%{version}.tar.gz
BuildRequires:  %{python_module pip}
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
Recommends:     %( ls /usr/lib*/libogg.so.*.*.* | sed -r 's/.*(libogg)\.so\.([0-9]*)\..*/\1\2/g' )
Recommends:     libflac
Recommends:     libvorbis
Recommends:     %( ls /usr/lib*/libopus.so.*.*.* | sed -r 's/.*(libopus)\.so\.([0-9]*)\..*/\1\2/g' )
Recommends:     %( ls /usr/lib*/libopusenc.so.*.*.* | sed -r 's/.*(libopusenc)\.so\.([0-9]*)\..*/\1\2/g' )
Recommends:     %( ls /usr/lib*/libopusfile.so.*.*.* | sed -r 's/.*(libopusfile)\.so\.([0-9]*)\..*/\1\2/g' )
Recommends:     %( ls /usr/lib*/libvorbisenc.so.*.*.* | sed -r 's/.*(libvorbisenc)\.so\.([0-9]*)\..*/\1\2/g' )
Recommends:     %( ls /usr/lib*/libvorbisfile.so.*.*.* | sed -r 's/.*(libvorbisfile)\.so\.([0-9]*)\..*/\1\2/g' )
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md README.rst
%license COPYING LICENSE
%{python_sitelib}/pyogg
%{python_sitelib}/PyOgg-%{version}.dist-info

%changelog
