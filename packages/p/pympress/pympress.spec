#
# spec file for package pympress
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


# The reverse-dns-like string used as app id and desktop file name
%define gtk_app_id io.github.pympress
# Do not support python 2, and build a single package
%define pythons python3
Name:           pympress
Version:        1.8.3
Release:        0
Summary:        A simple and powerful dual-screen PDF reader designed for presentations
License:        GPL-2.0-or-later
URL:            https://github.com/Cimbali/pympress/
Source0:        pympress-1.8.3.tar.gz
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-myst-parser
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools >= 42
BuildRequires:  python3-wheel
BuildRequires:  sed
BuildRequires:  update-desktop-files
Requires:       gobject-introspection
Requires:       gstreamer
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-plugins-good-gtk
Requires:       gtk3
Requires:       python(abi) >= 3.4
Requires:       python3-gobject
Requires:       python3-watchdog
Requires:       typelib(DBus)
Requires:       typelib(DBusGLib)
Requires:       typelib(GLib)
Requires:       typelib(GObject)
Requires:       typelib(Gdk)
Requires:       typelib(GdkPixbuf)
Requires:       typelib(Gio)
Requires:       typelib(Gst)
Requires:       typelib(GstAllocators)
Requires:       typelib(GstApp)
Requires:       typelib(GstAudio)
Requires:       typelib(GstVideo)
Requires:       typelib(Gtk)
Requires:       typelib(Poppler)
Requires:       typelib(cairo)
Requires(post): permissions
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-ugly
Recommends:     typelib(GstBadAudio)
Recommends:     typelib(GstCodecs)
Recommends:     typelib(GstMpegts)
Recommends:     typelib(GstWebRTC)
BuildArch:      noarch
%if %{python_version_nodots} < 39
Requires:       python3-importlib-resources
%endif

%description
Pympress is a PDF presentation tool designed for dual-screen setups such as
presentations and public talks.

Highly configurable, fully-featured, and portable, pympress comes with many
great features, including:
- supports embedded gifs, video, and audio
- text annotations displayed in the presenter window
- natively supports beamer's “notes on second screen”, as well as Libreoffice
  notes pages
- and much more

%prep
%setup -q -n pympress-%{version}

%build
%pyproject_wheel

# Build docs using options to skip devel docs (modules autodoc) which are in pympress.md and require resources that must be downloaded
# (sphinx extensions, intersphinx mappings from linked docs, etc), as well as installing instructions.
%python_exec -m sphinx -b html -d build/doctrees -Dskip_api_doc=1 -Dpackaged_docs=1 docs/ html/
%python_exec -m sphinx -b man  -d build/doctrees -Dskip_api_doc=1 -Dpackaged_docs=1 docs/ man/

%install
%pyproject_install

# Identify lang files
%find_lang pympress

%suse_update_desktop_file %{gtk_app_id}

mkdir -p %{buildroot}%{_mandir}/man1/
cp -av man/pympress.1 %{buildroot}%{_mandir}/man1/

# Also install docs to get them covered by fdupes
mkdir -p "%{buildroot}%{_defaultdocdir}/%{name}"
mv html/* "%{buildroot}%{_defaultdocdir}/%{name}/"

# Hardlink duplicate files, typically X.pyc and X.opt-1.pyc and pympress.png under /usr/share
# keep this specific so we still raise errors if we add a file twice
find "%{buildroot}%{python3_sitelib}/pympress/" -type d -name __pycache__ | xargs -L1 %fdupes
%fdupes "%{buildroot}%{_datadir}"

%post
%set_permissions %{_bindir}/pympress

# An old version distributed through copr listed files but not directories as installed files
# if upgrading, make sure to clean up these directories otherwise python is confused about what’s installed
if [ $1 -gt 1 ]; then
find "%{python3_sitelib}" -maxdepth 1 -name 'pympress-1.5.*' -print0 | xargs -0 --no-run-if-empty rm -r
fi

%files -f pympress.lang

# sitelib directories
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.dist-info

# out-of-sitelib files
%{_datadir}/applications/%{gtk_app_id}.desktop
%{_datadir}/pixmaps/%{name}.png
%verify(not mode) %attr(0755, root, root) %{_bindir}/pympress

# doc
%{_defaultdocdir}/%{name}
%{_mandir}/man1/%{name}.*
%license LICENSE.txt

%changelog
