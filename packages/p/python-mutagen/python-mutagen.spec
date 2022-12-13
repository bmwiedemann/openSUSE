#
# spec file for package python-mutagen
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
# Exception: Python 2 no longer supported
%define skip_python2 1
Name:           python-mutagen
Version:        1.46.0
Release:        0
Summary:        Python module to Handle Audio Metadata
License:        GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://pypi.python.org/pypi/mutagen
Source:         https://files.pythonhosted.org/packages/source/m/mutagen/mutagen-%{version}.tar.gz
# PATCH-FIX-OPENSUSE reduce-test-length.diff alarrosa@suse.com -- Reduce the number of iterations so tests don't take so long to finish
Patch0:         reduce-test-length.diff
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(preun):update-alternatives
%python_subpackages

%description
Mutagen is a Python module to handle audio metadata. It supports FLAC,
M4A, MP3, Ogg FLAC, Ogg Speex, Ogg Theora, Ogg Vorbis, True Audio, and
WavPack audio files. All versions of ID3v2 are supported, and all
standard ID3v2.4 frames are parsed. It can read Xing headers to
accurately calculate the bitrate and length of MP3s. ID3 and APEv2 tags
can be edited regardless of their audio format. It can also manipulate
Ogg streams on an individual packet/page level.

%prep
%setup -q -n mutagen-%{version}
%patch0 -p1
# remove shebangs from library files
find mutagen/ -name "*.py" -exec sed -i -e '/^#!\s\?\/usr\/bin\/\(env\s\)\?python$/d' {} ';'

%build
%python_build

%install
%python_install

for i in mid3cp mid3iconv mid3v2 moggsplit mutagen-inspect mutagen-pony; do
   %python_clone -a %{buildroot}%{_bindir}/${i}
   %python_clone -a %{buildroot}%{_mandir}/man1/${i}.1
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}/mutagen

%post
%{python_install_alternative mid3cp mid3iconv mid3v2 moggsplit mutagen-inspect mutagen-pony mid3cp.1 mid3iconv.1 mid3v2.1 moggsplit.1 mutagen-inspect.1 mutagen-pony.1}

%preun
%{python_uninstall_alternative mid3cp}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%defattr(-, root, root, 0755)
%license COPYING
%doc NEWS README.rst
%python_alternative %{_bindir}/mid3cp
%python_alternative %{_bindir}/mid3iconv
%python_alternative %{_bindir}/mid3v2
%python_alternative %{_bindir}/moggsplit
%python_alternative %{_bindir}/mutagen-inspect
%python_alternative %{_bindir}/mutagen-pony
%python_alternative %{_mandir}/man1/mid3cp.1%{ext_man}
%python_alternative %{_mandir}/man1/mid3iconv.1%{ext_man}
%python_alternative %{_mandir}/man1/mid3v2.1%{ext_man}
%python_alternative %{_mandir}/man1/moggsplit.1%{ext_man}
%python_alternative %{_mandir}/man1/mutagen-inspect.1%{ext_man}
%python_alternative %{_mandir}/man1/mutagen-pony.1%{ext_man}
%{python_sitelib}/mutagen
%{python_sitelib}/mutagen-%{version}-py%{python_version}.egg-info

%changelog
