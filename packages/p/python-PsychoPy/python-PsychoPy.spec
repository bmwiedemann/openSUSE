#
# spec file for package python-PsychoPy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-PsychoPy
Version:        3.2.4
Release:        0
License:        GPL-3.0-or-later
Summary:        Psychology experiment software in Python
Url:            https://github.com/psychopy/psychopy
Group:          Development/Languages/Python
Source:         https://github.com/psychopy/psychopy/releases/download/%{version}/PsychoPy-%{version}.zip
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python3-base > 3.5
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module SoundFile}
BuildRequires:  %{python_module arabic-reshaper}
BuildRequires:  %{python_module astunparse}
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module json_tricks}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module moviepy}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opencv}
BuildRequires:  %{python_module opengl}
BuildRequires:  %{python_module openpyxl}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pygame}
BuildRequires:  %{python_module pyglet}
BuildRequires:  %{python_module pyosf}
BuildRequires:  %{python_module pyparallel}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module python-bidi}
BuildRequires:  %{python_module python-gitlab}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module sounddevice}
BuildRequires:  %{python_module tables}
BuildRequires:  %{python_module wxPython}
BuildRequires:  %{python_module xlrd}
# /SECTION
Requires:       python-GitPython
Requires:       python-Pillow
Requires:       python-arabic-reshaper 
Requires:       python-astunparse
Requires:       python-configobj
Requires:       python-future
Requires:       python-json_tricks
Requires:       python-lxml
Requires:       python-matplotlib
Requires:       python-moviepy
Requires:       python-numpy
Requires:       python-opencv
Requires:       python-opengl
Requires:       python-openpyxl
Requires:       python-pandas
Requires:       python-pygame
Requires:       python-pyglet
Requires:       python-python-bidi
Requires:       python-python-gitlab
Requires:       python-pyzmq
Requires:       python-qt5
Requires:       python-scipy
Requires:       python-wxPython
Recommends:     python-PyYAML
Recommends:     python-SoundFile
Recommends:     python-cffi
Recommends:     python-gevent
Recommends:     python-greenlet
Recommends:     python-msgpack
Recommends:     python-psutil
Recommends:     python-psychtoolbox
Recommends:     python-pyosf
Recommends:     python-pyparallel
Recommends:     python-pyserial
Recommends:     python-requests
Recommends:     python-sounddevice
Recommends:     python-tables
Recommends:     python-xlrd
Requires:       python-Cython
%ifpython3
Requires:       python3-base >= 3.5
%endif
BuildArch:      noarch
Requires(post):   update-alternatives
Requires(postun):  update-alternatives

%python_subpackages

%description
PsychoPy is a package for running experiments in Python. PsychoPy
combines OpenGL with Python syntax in an attempt to give scientists a
stimulus presentation and control package.

%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Requires:       python-base
Provides:       %{name}-lang-all = %{version}

%description lang
Provides translations for the "%{name}" package.

%prep
%setup -q -n PsychoPy-%{version}
sed -i 's/\r$//' psychopy/CHANGELOG.txt
find -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/psychopy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
%python_expand cp psychopy/app/Resources/psychopy.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/PsychoPy-%{$python_bin_suffix}.png
# Can't use Science or Education categories right now, https://bugzilla.opensuse.org/show_bug.cgi?id=1074711
%python_expand %suse_update_desktop_file -c PsychoPy-%{$python_bin_suffix} "PsychoPy %{$python_bin_suffix}" "Psychology software in Python %{$python_bin_suffix}" "psychopy-%{$python_bin_suffix}" PsychoPy-%{$python_bin_suffix} Development IDE

rm -rf %{buildroot}%{_prefix}/psychojs.zip

# Deduplicating files can generate a RPMLINT warning for pyc mtime
%{python_expand $python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/psychopy/tests/test_app/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/psychopy/tests/test_app/
%fdupes %{buildroot}%{$python_sitelib}/psychopy/tests/test_app/
sed -i -e '1d;2i#!%__$python' %{buildroot}%{_bindir}/psychopy-%{$python_bin_suffix}
}

%find_lang %{name} --all-name %{name}.lang
%python_expand grep "%{$python_sitelib}" %{name}.lang > %{name}_%{$python_bin_suffix}.lang

%post
%python_install_alternative psychopy

%postun
%python_uninstall_alternative psychopy

%files %{python_files}
%doc README.md
%doc psychopy/CHANGELOG.txt
%license LICENSE
%license psychopy/LICENSE.txt
%license psychopy/LICENSES.txt
%python_alternative %{_bindir}/psychopy
%{_datadir}/icons/hicolor/256x256/apps/PsychoPy-%{python_bin_suffix}.png
%{_datadir}/applications/PsychoPy-%{python_bin_suffix}.desktop
%{python_sitelib}/psychopy/
%{python_sitelib}/PsychoPy-%{version}-py*.egg-info
%exclude %{python_sitelib}/psychopy/app/locale/*

%ifpython2
%files -n %{python2_prefix}-PsychoPy-lang -f %{name}_%{python2_bin_suffix}.lang
%license LICENSE
%license psychopy/LICENSE.txt
%license psychopy/LICENSES.txt
%dir %{python2_sitelib}/psychopy/app/locale/*/
%dir %{python2_sitelib}/psychopy/app/locale/*/LC_MESSAGE/
%endif

%ifpython3
%files -n %{python3_prefix}-PsychoPy-lang -f %{name}_%{python3_bin_suffix}.lang
%license LICENSE
%license psychopy/LICENSE.txt
%license psychopy/LICENSES.txt
%dir %{python3_sitelib}/psychopy/app/locale/*/
%dir %{python3_sitelib}/psychopy/app/locale/*/LC_MESSAGE/
%endif

%changelog
