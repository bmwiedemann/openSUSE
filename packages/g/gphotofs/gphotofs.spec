#
# spec file for package gphotofs
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


Name:           gphotofs
BuildRequires:  fuse3-devel
BuildRequires:  glib2-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
Requires:       fuse3
URL:            http://gphoto.sourceforge.net
%define prefix /usr
Summary:        User Level File System for gphoto-Based Cameras
License:        GPL-2.0-or-later
Group:          Hardware/Camera
Version:        1.0
Release:        0
Source0:        https://github.com/gphoto/gphotofs/releases/download/v1.0/gphotofs-%{version}.tar.bz2
Source1:        https://github.com/gphoto/gphotofs/releases/download/v1.0/gphotofs-%{version}.tar.bz2.asc
Source2:        gphotofs.keyring
Patch0:         gphotofs-fix-gcc15.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a fuse module to make digital cameras supported
by libgphoto2 visible as a file system.



Authors:
--------
    Scott Fritzinger <scottf@scs.unr.edu>
    Lutz Müller <lutz@users.sourceforge.net>

    Eugene Crosser <crosser@average.org>
    Matt Martin <matt.martin@ieee.org>
    Gary Ross <gdr@hooked.net>
    M. Adam Kendall <joker@penguinpub.com>
    Del Simmons <del@gphoto.org>
    Bob Paauwe <bpaauwe@bobsplace.com>
    Cliff Wright <cliff@snipe444.org>
    Phill Hugo <phill@gphoto.org>
    Beat Christen <spiff@longstreet.ch>
    Warren Baird <wjbaird@bigfoot.com>
    Brent D. Metz <bmetz@vt.edu>
    Brian Hirt <bhirt@loopy.berkhirt.com>
    Mandrake <mandrake@lobotomy.com>
    Randy D. Scott <scottr@wwa.com>
    Paul S. Jenner <psj@mustec.eu.org>
    Tuomas Kuosmanen <tigert@gimp.org>
    Ole Aamot <oleaa@ifi.uio.no>
    Mariusz Zynel <mariusz@mizar.org>
    Johannes Erdfelt <johannes@erdfelt.com>
    Werner Almesberger <almesber@lrc.di.epfl.ch>
    Ole W. Saastad <o.w.saastad@kjemi.uio.no>
    Veros Kaplan <xkaplan@informatics.muni.cz>
    Wolfgang Reissnegger
    Philippe Marzouk <philm@users.sourceforge.net>
    Edouard Lafargue <lafargue@oslo.geco-prakla.slb.com>
    Bart van Leeuwen <bart@netage.nl>
    M. Adam Kendall <joker@penguinpub.com>
    Mark Davies <mdavies@dial.pipex.com>
    Beat Christen <spiff@longstreet.ch>
    Gus Hartmann <hartmann@madison-expat.net>
    Raymond Penners <raymond@dotsphinx.com>
    Marcus Meissner <marcus@jet.franken.de>
    Hans Ulrich Niedermann <hun@users.sourceforge.net>
    Colin Marquardt <cmarqu@users.sourceforge.net>

%prep
%autosetup

%build
autoreconf -i -f
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS NEWS README
/usr/bin/gphotofs

%changelog
