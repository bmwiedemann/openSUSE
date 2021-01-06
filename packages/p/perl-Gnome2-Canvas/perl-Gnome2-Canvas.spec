#
# spec file for package perl-Gnome2-Canvas
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Gnome2-Canvas
Name:           perl-Gnome2-Canvas
Version:        1.006
Release:        0
#Upstream:  This library is free software; you can redistribute it and/or modify it under the terms of the GNU Library General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Library General Public License for more details. You should have received a copy of the GNU Library General Public License along with this library; if not, see <https://www.gnu.org/licenses>.
Summary:        (DEPRECATED) A structured graphics canvas
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Depends) >= 0.2
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.030000
BuildRequires:  perl(Glib) >= 1.120
BuildRequires:  perl(Gtk2) >= 1.100
Requires:       perl(ExtUtils::Depends) >= 0.200
Requires:       perl(ExtUtils::PkgConfig) >= 1.030000
Requires:       perl(Glib) >= 1.040
Requires:       perl(Gtk2) >= 1.040
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libgnomecanvas-devel
# MANUAL END

%description
*NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE*

This module has been deprecated by the Gtk-Perl project. This means that
the module will no longer be updated with security patches, bug fixes, or
when changes are made in the Perl ABI. The Git repo for this module has
been archived (made read-only), it will no longer possible to submit new
commits to it. You are more than welcome to ask about this module on the
Gtk-Perl mailing list, but our priorities going forward will be maintaining
Gtk-Perl modules that are supported and maintained upstream; this module is
neither.

Since this module is licensed under the LGPL v2.1, you may also fork this
module, if you wish, but you will need to use a different name for it on
CPAN, and the Gtk-Perl team requests that you use your own resources
(mailing list, Git repos, bug trackers, etc.) to maintain your fork going
forward.

  * Perl URL: https://gitlab.gnome.org/GNOME/perl-gnome2-canvas

  * Upstream URL: https://gitlab.gnome.org/Archive/libgnomecanvas

  * Last upstream version: 2.30.3

  * Last upstream release date: 2011-01-31

  * Migration path for this module: No upstream replacement

*NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE*

The Gnome Canvas is an engine for structured graphics that offers a rich
imaging model, high-performance rendering, and a powerful, high level API.
It offers a choice of two rendering back-ends, one based on GDK for
extremely fast display, and another based on Libart, a sophisticated,
antialiased, alpha-compositing engine. This widget can be used for flexible
display of graphics and for creating interactive user interface elements.

To create a new Gnome2::Canvas widget call 'Gnome2::Canvas->new' or
'Gnome2::Canvas->new_aa' for an anti-aliased mode canvas.

A Gnome2::Canvas contains one or more Gnome2::CanvasItem objects. Items
consist of graphing elements like lines, ellipses, polygons, images, text,
and curves. These items are organized using Gnome2::CanvasGroup objects,
which are themselves derived from Gnome2::CanvasItem. Since a group is an
item it can be contained within other groups, forming a tree of canvas
items. Certain operations, like translating and scaling, can be performed
on all items in a group.

There is a special root group created by a Gnome2::Canvas. This is the top
level group under which all items in a canvas are contained. The root group
is available as '$canvas->root'.

There are several different coordinate systems used by Gnome2::Canvas
widgets. The primary system is a logical, abstract coordinate space called
world coordinates. World coordinates are expressed as unbounded double
floating point numbers. When it comes to rendering to a screen the canvas
pixel coordinate system (also referred to as just canvas coordinates) is
used. This system uses integers to specify screen pixel positions. A user
defined scaling factor and offset are used to convert between world
coordinates and canvas coordinates. Each item in a canvas has its own
coordinate system called item coordinates. This system is specified in
world coordinates but they are relative to an item (0.0, 0.0 would be the
top left corner of the item). The final coordinate system of interest is
window coordinates. These are like canvas coordinates but are offsets from
within a window a canvas is displayed in. This last system is rarely used,
but is useful when manually handling GDK events (such as drag and drop)
which are specified in window coordinates (the events processed by the
canvas are already converted for you).

Along with different coordinate systems come methods to convert between
them. '$canvas->w2c' converts world to canvas pixel coordinates and
'canvas->c2w' converts from canvas to world. To get the affine transform
matrix for converting from world coordinates to canvas coordinates call
'$canvas->w2c_affine'. '$canvas->window_to_world' converts from window to
world coordinates and '$canvas->world_to_window' converts in the other
direction. There are no methods for converting between canvas and window
coordinates, since this is just a matter of subtracting the canvas
scrolling offset. To convert to/from item coordinates use the methods
defined for Gnome2::CanvasItem objects.

To set the canvas zoom factor (canvas pixels per world unit, the scaling
factor) call '$canvas->set_pixels_per_unit'; setting this to 1.0 will cause
the two coordinate systems to correspond (e.g., [5, 6] in pixel units would
be [5.0, 6.0] in world units).

Defining the scrollable area of a canvas widget is done by calling
'$canvas->set_scroll_region' and to get the current region
'$canvas->get_scroll_region' can be used. If the window is larger than the
canvas scrolling region it can optionally be centered in the window. Use
'$canvas->set_center_scroll_region' to enable or disable this behavior. To
scroll to a particular canvas pixel coordinate use '$canvas->scroll_to'
(typically not used since scrollbars are usually set up to handle the
scrolling), and to get the current canvas pixel scroll offset call
'$canvas->get_scroll_offsets'.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc AUTHORS canvas.typemap ChangeLog maps NEWS README TODO
%license LICENSE

%changelog
