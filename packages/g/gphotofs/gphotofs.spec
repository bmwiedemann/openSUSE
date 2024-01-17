#
# spec file for package gphotofs
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gphotofs
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libjpeg-devel
Requires:       fuse
Url:            http://gphoto.sourceforge.net
%define prefix /usr
Summary:        User Level File System for gphoto-Based Cameras
License:        GPL-2.0+
Group:          Hardware/Camera
Version:        0.5
Release:        0
Source0:        gphotofs-%{version}.tar.bz2
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
%setup -q

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
/usr/bin/gphotofs

%changelog
