#
# spec file for package python-wxPython
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
%define         oldpython python
%define         X_display ":98"
%bcond_with     test
%bcond_with     syswx
%if %{with syswx}
%define wx_args --use_syswx --gtk3 -v
%else
%define wx_args --gtk3 -v
%endif
Name:           python-wxPython
Version:        4.0.7.post1
Release:        0
Summary:        The "Phoenix" variant of the wxWidgets Python bindings
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/wxWidgets/Phoenix
Source:         https://files.pythonhosted.org/packages/source/w/wxPython/wxPython-%{version}.tar.gz
Source1:        python-wxPython-rpmlintrc
# PATCH-FIX-OPENSUSE fix_no_return_in_nonvoid.patch -- Fix lack of return in nonvoid functions
Patch0:         fix_no_return_in_nonvoid.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libjbig-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  xorg-x11-server
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(freeglut)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(x11)
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      python-wxWidgets
Provides:       python-wxWidgets = %{version}
%if %{with test}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%endif
%ifpython2
Conflicts:      %{oldpython}-wxWidgets
Provides:       %{oldpython}-wxWidgets = %{version}
%endif

%python_subpackages

%description
Phoenix is a reimplementation of wxPython. Like the "classic"
wxPython, Phoenix wraps the wxWidgets C++ toolkit and provides access
to the user interface portions of the wxWidgets API, enabling Python
applications to have a GUI on Windows, macOS or Unix-like systems,
with a native look and feel and requiring very little (if any)
platform specific code.

%package lang
# We cannot use %%lang_package here. Editra translations use noarch incompatible path.
Summary:        Languages for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Requires:       python-base
Supplements:    packageand(bundle-lang-other:%{name})
Provides:       %{name}-lang-all = %{version}

%description lang
Provides translations to the package %{name}.

%prep
%setup -q -n wxPython-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' wx/py/*.py
sed -i -e '/^#!\//, 1d' wx/tools/*.py
sed -i -e '/^#!\//, 1d' wx/py/tests/*.py

%build
export CFLAGS="%{optflags}"
export DOXYGEN=%{_bindir}/doxygen
%python_expand $python build.py build %{wx_args}

%install
%python_expand $python build.py install %{wx_args} --destdir=%{buildroot} --extra_setup="-O1 --force"

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%python_clone -a %{buildroot}%{_bindir}/helpviewer
%python_clone -a %{buildroot}%{_bindir}/img2png
%python_clone -a %{buildroot}%{_bindir}/img2py
%python_clone -a %{buildroot}%{_bindir}/img2xpm
%python_clone -a %{buildroot}%{_bindir}/pycrust
%python_clone -a %{buildroot}%{_bindir}/pyshell
%python_clone -a %{buildroot}%{_bindir}/pyslices
%python_clone -a %{buildroot}%{_bindir}/pyslicesshell
%python_clone -a %{buildroot}%{_bindir}/pywxrc
%python_clone -a %{buildroot}%{_bindir}/wxdemo
%python_clone -a %{buildroot}%{_bindir}/wxdocs
%python_clone -a %{buildroot}%{_bindir}/wxget

%if %{with test}
%check
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

rm -r build
rm -r _build*

mv wx wx_temp
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B build.py test %{wx_args}
}
mv wx_temp wx
%endif

%post
%{python_install_alternative pywxrc helpviewer img2png img2py img2xpm pycrust pyshell pyslices pyslicesshell wxdemo wxdocs wxget}

%postun
%python_uninstall_alternative pywxrc

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst TODO.rst license/*.txt
%python_alternative %{_bindir}/helpviewer
%python_alternative %{_bindir}/img2png
%python_alternative %{_bindir}/img2py
%python_alternative %{_bindir}/img2xpm
%python_alternative %{_bindir}/pycrust
%python_alternative %{_bindir}/pyshell
%python_alternative %{_bindir}/pyslices
%python_alternative %{_bindir}/pyslicesshell
%python_alternative %{_bindir}/pywxrc
%python_alternative %{_bindir}/wxdemo
%python_alternative %{_bindir}/wxdocs
%python_alternative %{_bindir}/wxget
%{python_sitearch}/wxPython-%{version}-py*.egg-info
%{python_sitearch}/wx/
%exclude %{python_sitearch}/wx/locale/

%files %{python_files lang}
%{python_sitearch}/wx/locale/

%changelog
