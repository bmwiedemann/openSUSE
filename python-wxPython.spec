#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define         X_display ":98"
%bcond_without  test
%bcond_without  syswx
# We rebuild the ETG and SIP files for two reasons:
# - Fixing a bug in the ETG time_t typedef (see patch)
# - Compatibility with SIP 6.5.x, for Leap 15.x
%bcond_without  rebuild_sip

%if %{with syswx}
%define wx_args --use_syswx --gtk3 -v
%else
%define wx_args --gtk3 -v
%endif

%global flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == ""
# factory-auto requires the main build_flavor to match the specfile name
%define pprefix python
%define python_module() no-build-without-multibuild-flavor
ExclusiveArch:  donotbuild
%else
%define pprefix %flavor
%if 0%{suse_version} >= 1599
# Tumbleweed has a varying number of python3 flavors. The flavor
# selection here and in _multibuild must be kept in sync with the Factory
# prjconf definition for pythons. If a skip is missing, all builds fail.
# Extraneous build_flavors and skips are excluded automatically so future
# additions can be included here early and old flavors can be removed some time
# after the global drop in Factory.
%if "%flavor" != "python38"
%define skip_python38 1
%endif
%if "%flavor" != "python39"
%define skip_python39 1
%endif
%if "%flavor" != "python310"
%define skip_python310 1
%endif
%if "%flavor" != "python311"
%define skip_python311 1
%endif
%else
# SLE/Leap: python3 only
%if "%flavor" != "python3"
%define pythons %{nil}
%else
%define pythons python3
%define python3_provides %{nil}
%endif
%endif
# The obs server-side interpreter cannot use lua or rpm shrink
%if "%pythons" == "" || "%pythons" == " " || "%pythons" == "  " || "%pythons" == "   " || "%pythons" == "    "
ExclusiveArch:  donotbuild
%define python_module() %flavor-not-enabled-in-buildset-for-suse-%{?suse_version}
%else
%define python_files() -n %flavor-%{**}
%define python_module() %flavor-%{**}
%define python_exec python%{expand:%%%{flavor}_bin_suffix}
%define python_version %{expand:%%%{flavor}_version}
%define python_sitearch %{expand:%%%{flavor}_sitearch}
%define python_provides %{expand:%%%{flavor}_provides}
%endif
%endif

Name:           %{pprefix}-wxPython
Version:        4.2.0
Release:        0
Summary:        The "Phoenix" variant of the wxWidgets Python bindings
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://github.com/wxWidgets/Phoenix
Source:         https://files.pythonhosted.org/packages/source/w/wxPython/wxPython-%{version}.tar.gz
Source1:        python-wxPython-rpmlintrc
# PATCH-FIX-OPENSUSE
Patch1:         use_stl_build.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Only-import-attrdict-where-needed.patch
# PATCH-FIX-UPSTREAM - https://github.com/wxWidgets/Phoenix/pull/2232
Patch4:         0003-Make-pip-usage-in-wxget-optional.patch
# PATCH-FIX-OPENSUSE
Patch5:         0004-Fix-time_t-ETG-typedef-extend-DateTime.FromTimeT-tes.patch
# PATCH-FIX-OPENSUSE - Test fixes/additions:
Patch112:       0001-Check-HSV-values-in-image-test.patch
# PATCH-FIX-UPSTREAM - https://github.com/wxWidgets/Phoenix/pull/2233
Patch113:       0001-Fix-overflow-check-for-wxUIntPtr-type.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if %{with syswx}
BuildRequires:  %{python_module sip6-devel >= 6.5.1}
BuildRequires:  waf
BuildRequires:  wxGTK3-devel >= 3.2.0
BuildRequires:  wxWidgets-3_2-doc-xml >= 3.2.0
%else
BuildRequires:  freeglut-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libjbig-devel
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
BuildRequires:  pkgconfig(xtst)
%endif
Requires:       %{pprefix}-six
Requires(post): update-alternatives
Requires(postun):update-alternatives
Conflicts:      %{pprefix}-wxWidgets
Provides:       %{pprefix}-wxWidgets = %{version}
%if "%{python_provides}" != ""
# for TW primary flavor provider
Conflicts:      %{python_provides}-wxWidgets
Provides:       %{python_provides}-wxPython = %{version}-%{release}
Provides:       %{python_provides}-wxWidgets = %{version}
Obsoletes:      %{python_provides}-wxPython < %{version}-%{release}
%endif
%if %{with test}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  Mesa-dri
# Need at least one font installed
BuildRequires:  google-opensans-fonts
# BuildRequires:  wxWidgets-lang
BuildRequires:  xorg-x11-server
BuildRequires:  pkgconfig(cppunit)
%endif

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
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires:       python(abi) = %python_version
Supplements:    (bundle-lang-other and %{name})
Provides:       %{name}-lang-all = %{version}
%if "%{python_provides}" != ""
# for TW primary flavor provider
Provides:       %{python_provides}-wxPython-lang = %{version}-%{release}
Obsoletes:      %{python_provides}-wxPython-lang < %{version}-%{release}
%endif

%description lang
Provides translations to the package %{name}.

%prep
%autosetup -n wxPython-%{version} -p1
# Lower minimum Python version
sed -i -e '/check_python_version/ s@3,7,0@3,6,0@' wscript

# Reuse locale from wxWidgets package
%if %{with syswx}
rm -Rf wx/locale
%endif

sed -i -e '/^#!\//, 1d' wx/py/*.py
sed -i -e '/^#!\//, 1d' wx/tools/*.py
sed -i -e '/^#!\//, 1d' wx/py/tests/*.py
echo "# empty module" >> wx/lib/pubsub/core/itopicdefnprovider.py

%build
export CFLAGS="%{optflags}"

%if %{with rebuild_sip}
# Save LICENSE* files from bundled siplib
mv sip/siplib{,_old}

export DOXYGEN=%{_bindir}/doxygen
export SIP=%{_bindir}/sip
export WAF=%{_bindir}/waf
mkdir -p /tmp/wxxml/docs/doxygen/out/
rm -f /tmp/wxxml/docs/doxygen/out/xml
cp ext/wxWidgets/docs/*.txt /tmp/wxxml/docs/
ln -sf %{_docdir}/wxWidgets*doc-xml /tmp/wxxml/docs/doxygen/out/xml
export WXWIN=/tmp/wxxml/

%python_exec build.py touch %{wx_args}
%python_exec build.py etg --nodoc %{wx_args}
%python_exec build.py sip %{wx_args}
cp sip/siplib_old/LICENSE* sip/siplib/
if [ ! -e sip/siplib/sip_array.c ]; then
  cp sip/siplib/{,sip_}array.c
  cp sip/siplib/{,sip_}array.h
fi
%endif

%python_exec build.py build %{wx_args}

%install
%python_exec build.py install %{wx_args} --destdir=%{buildroot} --extra_setup="-O1 --force"

%fdupes %{buildroot}%{_libdir}

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

%if %{without syswx}
%find_lang wxstd
%endif

%check
%if %{with test}
#############################################
### Launch a virtual framebuffer X server ###
#############################################
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 5

# Make sure "import wx" does not confuse the wx dir with the module
mv wx wx_temp

# pytest --forked from python-pytest-forked:
# Run each test as a separate process, otherwise multiple app
# instances will corrupt each others static data.
#
# Run UiAction tests one by one
%pytest_arch --forked -n 1 -k 'test_uiaction or test_mousemanager' unittests/
# Skip Auto ID management test (only enabled on Windows)
# Skip Frame restore (requires a window manager)
# Skip Locale.GetString, we do not ship translations for wxWidgets-3_2
# Skip wx.lib.pubsub, fails due to PYTHONDONTWRITEBYTECODE, also deprecated for pypubsub
# Skip UiAction tests (already done)
%{pytest_arch --forked -n 4 -k \
  '(not test_newIdRef03) and (not test_uiaction) and (not test_mousemanager) and (not test_frameRestore) and (not test_intlGetString) and (not lib_pubsub_Except) and (not test_xrc7)' \
  unittests/
}

mv wx_temp wx
%endif

%post
%python_install_alternative pywxrc helpviewer img2png img2py img2xpm pycrust pyshell pyslices pyslicesshell wxdemo wxdocs wxget

%postun
%python_uninstall_alternative pywxrc

%files
%license LICENSE.txt license/*.txt
%doc CHANGES.rst README.rst TODO.rst
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
%{python_sitearch}/wxPython-*-py*.egg-info
%{python_sitearch}/wx/
%if %{without syswx}
%exclude %{python_sitearch}/wx/locale/
%endif

%if %{without syswx}
%files lang -f wxstd.lang
%dir %{python_sitearch}/wx/locale/
%dir %{python_sitearch}/wx/locale/*
%dir %{python_sitearch}/wx/locale/*/LC_MESSAGES
%endif

%changelog
