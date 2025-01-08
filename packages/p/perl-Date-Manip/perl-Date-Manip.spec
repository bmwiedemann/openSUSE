#
# spec file for package perl-Date-Manip
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Date-Manip
Name:           perl-Date-Manip
Version:        6.960.0
Release:        0
# 6.96 -> normalize -> 6.960.0
%define cpan_version 6.96
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Date manipulation routines
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.67
BuildRequires:  perl(Test::Inter) >= 1.09
Provides:       perl(Date::Manip) = %{version}
Provides:       perl(Date::Manip::Base) = %{version}
Provides:       perl(Date::Manip::DM5) = %{version}
Provides:       perl(Date::Manip::DM5abbrevs) = %{version}
Provides:       perl(Date::Manip::DM6) = %{version}
Provides:       perl(Date::Manip::Date) = %{version}
Provides:       perl(Date::Manip::Delta) = %{version}
Provides:       perl(Date::Manip::Lang::catalan) = %{version}
Provides:       perl(Date::Manip::Lang::danish) = %{version}
Provides:       perl(Date::Manip::Lang::dutch) = %{version}
Provides:       perl(Date::Manip::Lang::english) = %{version}
Provides:       perl(Date::Manip::Lang::finnish) = %{version}
Provides:       perl(Date::Manip::Lang::french) = %{version}
Provides:       perl(Date::Manip::Lang::german) = %{version}
Provides:       perl(Date::Manip::Lang::index) = %{version}
Provides:       perl(Date::Manip::Lang::italian) = %{version}
Provides:       perl(Date::Manip::Lang::norwegian) = %{version}
Provides:       perl(Date::Manip::Lang::polish) = %{version}
Provides:       perl(Date::Manip::Lang::portugue) = %{version}
Provides:       perl(Date::Manip::Lang::romanian) = %{version}
Provides:       perl(Date::Manip::Lang::russian) = %{version}
Provides:       perl(Date::Manip::Lang::spanish) = %{version}
Provides:       perl(Date::Manip::Lang::swedish) = %{version}
Provides:       perl(Date::Manip::Lang::turkish) = %{version}
Provides:       perl(Date::Manip::Obj) = %{version}
Provides:       perl(Date::Manip::Offset::off000) = %{version}
Provides:       perl(Date::Manip::Offset::off001) = %{version}
Provides:       perl(Date::Manip::Offset::off002) = %{version}
Provides:       perl(Date::Manip::Offset::off003) = %{version}
Provides:       perl(Date::Manip::Offset::off004) = %{version}
Provides:       perl(Date::Manip::Offset::off005) = %{version}
Provides:       perl(Date::Manip::Offset::off006) = %{version}
Provides:       perl(Date::Manip::Offset::off007) = %{version}
Provides:       perl(Date::Manip::Offset::off008) = %{version}
Provides:       perl(Date::Manip::Offset::off009) = %{version}
Provides:       perl(Date::Manip::Offset::off010) = %{version}
Provides:       perl(Date::Manip::Offset::off011) = %{version}
Provides:       perl(Date::Manip::Offset::off012) = %{version}
Provides:       perl(Date::Manip::Offset::off013) = %{version}
Provides:       perl(Date::Manip::Offset::off014) = %{version}
Provides:       perl(Date::Manip::Offset::off015) = %{version}
Provides:       perl(Date::Manip::Offset::off016) = %{version}
Provides:       perl(Date::Manip::Offset::off017) = %{version}
Provides:       perl(Date::Manip::Offset::off018) = %{version}
Provides:       perl(Date::Manip::Offset::off019) = %{version}
Provides:       perl(Date::Manip::Offset::off020) = %{version}
Provides:       perl(Date::Manip::Offset::off021) = %{version}
Provides:       perl(Date::Manip::Offset::off022) = %{version}
Provides:       perl(Date::Manip::Offset::off023) = %{version}
Provides:       perl(Date::Manip::Offset::off024) = %{version}
Provides:       perl(Date::Manip::Offset::off025) = %{version}
Provides:       perl(Date::Manip::Offset::off026) = %{version}
Provides:       perl(Date::Manip::Offset::off027) = %{version}
Provides:       perl(Date::Manip::Offset::off028) = %{version}
Provides:       perl(Date::Manip::Offset::off029) = %{version}
Provides:       perl(Date::Manip::Offset::off030) = %{version}
Provides:       perl(Date::Manip::Offset::off031) = %{version}
Provides:       perl(Date::Manip::Offset::off032) = %{version}
Provides:       perl(Date::Manip::Offset::off033) = %{version}
Provides:       perl(Date::Manip::Offset::off034) = %{version}
Provides:       perl(Date::Manip::Offset::off035) = %{version}
Provides:       perl(Date::Manip::Offset::off036) = %{version}
Provides:       perl(Date::Manip::Offset::off037) = %{version}
Provides:       perl(Date::Manip::Offset::off038) = %{version}
Provides:       perl(Date::Manip::Offset::off039) = %{version}
Provides:       perl(Date::Manip::Offset::off040) = %{version}
Provides:       perl(Date::Manip::Offset::off041) = %{version}
Provides:       perl(Date::Manip::Offset::off042) = %{version}
Provides:       perl(Date::Manip::Offset::off043) = %{version}
Provides:       perl(Date::Manip::Offset::off044) = %{version}
Provides:       perl(Date::Manip::Offset::off045) = %{version}
Provides:       perl(Date::Manip::Offset::off046) = %{version}
Provides:       perl(Date::Manip::Offset::off047) = %{version}
Provides:       perl(Date::Manip::Offset::off048) = %{version}
Provides:       perl(Date::Manip::Offset::off049) = %{version}
Provides:       perl(Date::Manip::Offset::off050) = %{version}
Provides:       perl(Date::Manip::Offset::off051) = %{version}
Provides:       perl(Date::Manip::Offset::off052) = %{version}
Provides:       perl(Date::Manip::Offset::off053) = %{version}
Provides:       perl(Date::Manip::Offset::off054) = %{version}
Provides:       perl(Date::Manip::Offset::off055) = %{version}
Provides:       perl(Date::Manip::Offset::off056) = %{version}
Provides:       perl(Date::Manip::Offset::off057) = %{version}
Provides:       perl(Date::Manip::Offset::off058) = %{version}
Provides:       perl(Date::Manip::Offset::off059) = %{version}
Provides:       perl(Date::Manip::Offset::off060) = %{version}
Provides:       perl(Date::Manip::Offset::off061) = %{version}
Provides:       perl(Date::Manip::Offset::off062) = %{version}
Provides:       perl(Date::Manip::Offset::off063) = %{version}
Provides:       perl(Date::Manip::Offset::off064) = %{version}
Provides:       perl(Date::Manip::Offset::off065) = %{version}
Provides:       perl(Date::Manip::Offset::off066) = %{version}
Provides:       perl(Date::Manip::Offset::off067) = %{version}
Provides:       perl(Date::Manip::Offset::off068) = %{version}
Provides:       perl(Date::Manip::Offset::off069) = %{version}
Provides:       perl(Date::Manip::Offset::off070) = %{version}
Provides:       perl(Date::Manip::Offset::off071) = %{version}
Provides:       perl(Date::Manip::Offset::off072) = %{version}
Provides:       perl(Date::Manip::Offset::off073) = %{version}
Provides:       perl(Date::Manip::Offset::off074) = %{version}
Provides:       perl(Date::Manip::Offset::off075) = %{version}
Provides:       perl(Date::Manip::Offset::off076) = %{version}
Provides:       perl(Date::Manip::Offset::off077) = %{version}
Provides:       perl(Date::Manip::Offset::off078) = %{version}
Provides:       perl(Date::Manip::Offset::off079) = %{version}
Provides:       perl(Date::Manip::Offset::off080) = %{version}
Provides:       perl(Date::Manip::Offset::off081) = %{version}
Provides:       perl(Date::Manip::Offset::off082) = %{version}
Provides:       perl(Date::Manip::Offset::off083) = %{version}
Provides:       perl(Date::Manip::Offset::off084) = %{version}
Provides:       perl(Date::Manip::Offset::off085) = %{version}
Provides:       perl(Date::Manip::Offset::off086) = %{version}
Provides:       perl(Date::Manip::Offset::off087) = %{version}
Provides:       perl(Date::Manip::Offset::off088) = %{version}
Provides:       perl(Date::Manip::Offset::off089) = %{version}
Provides:       perl(Date::Manip::Offset::off090) = %{version}
Provides:       perl(Date::Manip::Offset::off091) = %{version}
Provides:       perl(Date::Manip::Offset::off092) = %{version}
Provides:       perl(Date::Manip::Offset::off093) = %{version}
Provides:       perl(Date::Manip::Offset::off094) = %{version}
Provides:       perl(Date::Manip::Offset::off095) = %{version}
Provides:       perl(Date::Manip::Offset::off096) = %{version}
Provides:       perl(Date::Manip::Offset::off097) = %{version}
Provides:       perl(Date::Manip::Offset::off098) = %{version}
Provides:       perl(Date::Manip::Offset::off099) = %{version}
Provides:       perl(Date::Manip::Offset::off100) = %{version}
Provides:       perl(Date::Manip::Offset::off101) = %{version}
Provides:       perl(Date::Manip::Offset::off102) = %{version}
Provides:       perl(Date::Manip::Offset::off103) = %{version}
Provides:       perl(Date::Manip::Offset::off104) = %{version}
Provides:       perl(Date::Manip::Offset::off105) = %{version}
Provides:       perl(Date::Manip::Offset::off106) = %{version}
Provides:       perl(Date::Manip::Offset::off107) = %{version}
Provides:       perl(Date::Manip::Offset::off108) = %{version}
Provides:       perl(Date::Manip::Offset::off109) = %{version}
Provides:       perl(Date::Manip::Offset::off110) = %{version}
Provides:       perl(Date::Manip::Offset::off111) = %{version}
Provides:       perl(Date::Manip::Offset::off112) = %{version}
Provides:       perl(Date::Manip::Offset::off113) = %{version}
Provides:       perl(Date::Manip::Offset::off114) = %{version}
Provides:       perl(Date::Manip::Offset::off115) = %{version}
Provides:       perl(Date::Manip::Offset::off116) = %{version}
Provides:       perl(Date::Manip::Offset::off117) = %{version}
Provides:       perl(Date::Manip::Offset::off118) = %{version}
Provides:       perl(Date::Manip::Offset::off119) = %{version}
Provides:       perl(Date::Manip::Offset::off120) = %{version}
Provides:       perl(Date::Manip::Offset::off121) = %{version}
Provides:       perl(Date::Manip::Offset::off122) = %{version}
Provides:       perl(Date::Manip::Offset::off123) = %{version}
Provides:       perl(Date::Manip::Offset::off124) = %{version}
Provides:       perl(Date::Manip::Offset::off125) = %{version}
Provides:       perl(Date::Manip::Offset::off126) = %{version}
Provides:       perl(Date::Manip::Offset::off127) = %{version}
Provides:       perl(Date::Manip::Offset::off128) = %{version}
Provides:       perl(Date::Manip::Offset::off129) = %{version}
Provides:       perl(Date::Manip::Offset::off130) = %{version}
Provides:       perl(Date::Manip::Offset::off131) = %{version}
Provides:       perl(Date::Manip::Offset::off132) = %{version}
Provides:       perl(Date::Manip::Offset::off133) = %{version}
Provides:       perl(Date::Manip::Offset::off134) = %{version}
Provides:       perl(Date::Manip::Offset::off135) = %{version}
Provides:       perl(Date::Manip::Offset::off136) = %{version}
Provides:       perl(Date::Manip::Offset::off137) = %{version}
Provides:       perl(Date::Manip::Offset::off138) = %{version}
Provides:       perl(Date::Manip::Offset::off139) = %{version}
Provides:       perl(Date::Manip::Offset::off140) = %{version}
Provides:       perl(Date::Manip::Offset::off141) = %{version}
Provides:       perl(Date::Manip::Offset::off142) = %{version}
Provides:       perl(Date::Manip::Offset::off143) = %{version}
Provides:       perl(Date::Manip::Offset::off144) = %{version}
Provides:       perl(Date::Manip::Offset::off145) = %{version}
Provides:       perl(Date::Manip::Offset::off146) = %{version}
Provides:       perl(Date::Manip::Offset::off147) = %{version}
Provides:       perl(Date::Manip::Offset::off148) = %{version}
Provides:       perl(Date::Manip::Offset::off149) = %{version}
Provides:       perl(Date::Manip::Offset::off150) = %{version}
Provides:       perl(Date::Manip::Offset::off151) = %{version}
Provides:       perl(Date::Manip::Offset::off152) = %{version}
Provides:       perl(Date::Manip::Offset::off153) = %{version}
Provides:       perl(Date::Manip::Offset::off154) = %{version}
Provides:       perl(Date::Manip::Offset::off155) = %{version}
Provides:       perl(Date::Manip::Offset::off156) = %{version}
Provides:       perl(Date::Manip::Offset::off157) = %{version}
Provides:       perl(Date::Manip::Offset::off158) = %{version}
Provides:       perl(Date::Manip::Offset::off159) = %{version}
Provides:       perl(Date::Manip::Offset::off160) = %{version}
Provides:       perl(Date::Manip::Offset::off161) = %{version}
Provides:       perl(Date::Manip::Offset::off162) = %{version}
Provides:       perl(Date::Manip::Offset::off163) = %{version}
Provides:       perl(Date::Manip::Offset::off164) = %{version}
Provides:       perl(Date::Manip::Offset::off165) = %{version}
Provides:       perl(Date::Manip::Offset::off166) = %{version}
Provides:       perl(Date::Manip::Offset::off167) = %{version}
Provides:       perl(Date::Manip::Offset::off168) = %{version}
Provides:       perl(Date::Manip::Offset::off169) = %{version}
Provides:       perl(Date::Manip::Offset::off170) = %{version}
Provides:       perl(Date::Manip::Offset::off171) = %{version}
Provides:       perl(Date::Manip::Offset::off172) = %{version}
Provides:       perl(Date::Manip::Offset::off173) = %{version}
Provides:       perl(Date::Manip::Offset::off174) = %{version}
Provides:       perl(Date::Manip::Offset::off175) = %{version}
Provides:       perl(Date::Manip::Offset::off176) = %{version}
Provides:       perl(Date::Manip::Offset::off177) = %{version}
Provides:       perl(Date::Manip::Offset::off178) = %{version}
Provides:       perl(Date::Manip::Offset::off179) = %{version}
Provides:       perl(Date::Manip::Offset::off180) = %{version}
Provides:       perl(Date::Manip::Offset::off181) = %{version}
Provides:       perl(Date::Manip::Offset::off182) = %{version}
Provides:       perl(Date::Manip::Offset::off183) = %{version}
Provides:       perl(Date::Manip::Offset::off184) = %{version}
Provides:       perl(Date::Manip::Offset::off185) = %{version}
Provides:       perl(Date::Manip::Offset::off186) = %{version}
Provides:       perl(Date::Manip::Offset::off187) = %{version}
Provides:       perl(Date::Manip::Offset::off188) = %{version}
Provides:       perl(Date::Manip::Offset::off189) = %{version}
Provides:       perl(Date::Manip::Offset::off190) = %{version}
Provides:       perl(Date::Manip::Offset::off191) = %{version}
Provides:       perl(Date::Manip::Offset::off192) = %{version}
Provides:       perl(Date::Manip::Offset::off193) = %{version}
Provides:       perl(Date::Manip::Offset::off194) = %{version}
Provides:       perl(Date::Manip::Offset::off195) = %{version}
Provides:       perl(Date::Manip::Offset::off196) = %{version}
Provides:       perl(Date::Manip::Offset::off197) = %{version}
Provides:       perl(Date::Manip::Offset::off198) = %{version}
Provides:       perl(Date::Manip::Offset::off199) = %{version}
Provides:       perl(Date::Manip::Offset::off200) = %{version}
Provides:       perl(Date::Manip::Offset::off201) = %{version}
Provides:       perl(Date::Manip::Offset::off202) = %{version}
Provides:       perl(Date::Manip::Offset::off203) = %{version}
Provides:       perl(Date::Manip::Offset::off204) = %{version}
Provides:       perl(Date::Manip::Offset::off205) = %{version}
Provides:       perl(Date::Manip::Offset::off206) = %{version}
Provides:       perl(Date::Manip::Offset::off207) = %{version}
Provides:       perl(Date::Manip::Offset::off208) = %{version}
Provides:       perl(Date::Manip::Offset::off209) = %{version}
Provides:       perl(Date::Manip::Offset::off210) = %{version}
Provides:       perl(Date::Manip::Offset::off211) = %{version}
Provides:       perl(Date::Manip::Offset::off212) = %{version}
Provides:       perl(Date::Manip::Offset::off213) = %{version}
Provides:       perl(Date::Manip::Offset::off214) = %{version}
Provides:       perl(Date::Manip::Offset::off215) = %{version}
Provides:       perl(Date::Manip::Offset::off216) = %{version}
Provides:       perl(Date::Manip::Offset::off217) = %{version}
Provides:       perl(Date::Manip::Offset::off218) = %{version}
Provides:       perl(Date::Manip::Offset::off219) = %{version}
Provides:       perl(Date::Manip::Offset::off220) = %{version}
Provides:       perl(Date::Manip::Offset::off221) = %{version}
Provides:       perl(Date::Manip::Offset::off222) = %{version}
Provides:       perl(Date::Manip::Offset::off223) = %{version}
Provides:       perl(Date::Manip::Offset::off224) = %{version}
Provides:       perl(Date::Manip::Offset::off225) = %{version}
Provides:       perl(Date::Manip::Offset::off226) = %{version}
Provides:       perl(Date::Manip::Offset::off227) = %{version}
Provides:       perl(Date::Manip::Offset::off228) = %{version}
Provides:       perl(Date::Manip::Offset::off229) = %{version}
Provides:       perl(Date::Manip::Offset::off230) = %{version}
Provides:       perl(Date::Manip::Offset::off231) = %{version}
Provides:       perl(Date::Manip::Offset::off232) = %{version}
Provides:       perl(Date::Manip::Offset::off233) = %{version}
Provides:       perl(Date::Manip::Offset::off234) = %{version}
Provides:       perl(Date::Manip::Offset::off235) = %{version}
Provides:       perl(Date::Manip::Offset::off236) = %{version}
Provides:       perl(Date::Manip::Offset::off237) = %{version}
Provides:       perl(Date::Manip::Offset::off238) = %{version}
Provides:       perl(Date::Manip::Offset::off239) = %{version}
Provides:       perl(Date::Manip::Offset::off240) = %{version}
Provides:       perl(Date::Manip::Offset::off241) = %{version}
Provides:       perl(Date::Manip::Offset::off242) = %{version}
Provides:       perl(Date::Manip::Offset::off243) = %{version}
Provides:       perl(Date::Manip::Offset::off244) = %{version}
Provides:       perl(Date::Manip::Offset::off245) = %{version}
Provides:       perl(Date::Manip::Offset::off246) = %{version}
Provides:       perl(Date::Manip::Offset::off247) = %{version}
Provides:       perl(Date::Manip::Offset::off248) = %{version}
Provides:       perl(Date::Manip::Offset::off249) = %{version}
Provides:       perl(Date::Manip::Offset::off250) = %{version}
Provides:       perl(Date::Manip::Offset::off251) = %{version}
Provides:       perl(Date::Manip::Offset::off252) = %{version}
Provides:       perl(Date::Manip::Offset::off253) = %{version}
Provides:       perl(Date::Manip::Offset::off254) = %{version}
Provides:       perl(Date::Manip::Offset::off255) = %{version}
Provides:       perl(Date::Manip::Offset::off256) = %{version}
Provides:       perl(Date::Manip::Offset::off257) = %{version}
Provides:       perl(Date::Manip::Offset::off258) = %{version}
Provides:       perl(Date::Manip::Offset::off259) = %{version}
Provides:       perl(Date::Manip::Offset::off260) = %{version}
Provides:       perl(Date::Manip::Offset::off261) = %{version}
Provides:       perl(Date::Manip::Offset::off262) = %{version}
Provides:       perl(Date::Manip::Offset::off263) = %{version}
Provides:       perl(Date::Manip::Offset::off264) = %{version}
Provides:       perl(Date::Manip::Offset::off265) = %{version}
Provides:       perl(Date::Manip::Offset::off266) = %{version}
Provides:       perl(Date::Manip::Offset::off267) = %{version}
Provides:       perl(Date::Manip::Offset::off268) = %{version}
Provides:       perl(Date::Manip::Offset::off269) = %{version}
Provides:       perl(Date::Manip::Offset::off270) = %{version}
Provides:       perl(Date::Manip::Offset::off271) = %{version}
Provides:       perl(Date::Manip::Offset::off272) = %{version}
Provides:       perl(Date::Manip::Offset::off273) = %{version}
Provides:       perl(Date::Manip::Offset::off274) = %{version}
Provides:       perl(Date::Manip::Offset::off275) = %{version}
Provides:       perl(Date::Manip::Offset::off276) = %{version}
Provides:       perl(Date::Manip::Offset::off277) = %{version}
Provides:       perl(Date::Manip::Offset::off278) = %{version}
Provides:       perl(Date::Manip::Offset::off279) = %{version}
Provides:       perl(Date::Manip::Offset::off280) = %{version}
Provides:       perl(Date::Manip::Offset::off281) = %{version}
Provides:       perl(Date::Manip::Offset::off282) = %{version}
Provides:       perl(Date::Manip::Offset::off283) = %{version}
Provides:       perl(Date::Manip::Offset::off284) = %{version}
Provides:       perl(Date::Manip::Offset::off285) = %{version}
Provides:       perl(Date::Manip::Offset::off286) = %{version}
Provides:       perl(Date::Manip::Offset::off287) = %{version}
Provides:       perl(Date::Manip::Offset::off288) = %{version}
Provides:       perl(Date::Manip::Offset::off289) = %{version}
Provides:       perl(Date::Manip::Offset::off290) = %{version}
Provides:       perl(Date::Manip::Offset::off291) = %{version}
Provides:       perl(Date::Manip::Offset::off292) = %{version}
Provides:       perl(Date::Manip::Offset::off293) = %{version}
Provides:       perl(Date::Manip::Offset::off294) = %{version}
Provides:       perl(Date::Manip::Offset::off295) = %{version}
Provides:       perl(Date::Manip::Offset::off296) = %{version}
Provides:       perl(Date::Manip::Offset::off297) = %{version}
Provides:       perl(Date::Manip::Offset::off298) = %{version}
Provides:       perl(Date::Manip::Offset::off299) = %{version}
Provides:       perl(Date::Manip::Offset::off300) = %{version}
Provides:       perl(Date::Manip::Offset::off301) = %{version}
Provides:       perl(Date::Manip::Offset::off302) = %{version}
Provides:       perl(Date::Manip::Offset::off303) = %{version}
Provides:       perl(Date::Manip::Offset::off304) = %{version}
Provides:       perl(Date::Manip::Offset::off305) = %{version}
Provides:       perl(Date::Manip::Offset::off306) = %{version}
Provides:       perl(Date::Manip::Offset::off307) = %{version}
Provides:       perl(Date::Manip::Offset::off308) = %{version}
Provides:       perl(Date::Manip::Offset::off309) = %{version}
Provides:       perl(Date::Manip::Offset::off310) = %{version}
Provides:       perl(Date::Manip::Offset::off311) = %{version}
Provides:       perl(Date::Manip::Offset::off312) = %{version}
Provides:       perl(Date::Manip::Offset::off313) = %{version}
Provides:       perl(Date::Manip::Offset::off314) = %{version}
Provides:       perl(Date::Manip::Offset::off315) = %{version}
Provides:       perl(Date::Manip::Offset::off316) = %{version}
Provides:       perl(Date::Manip::Offset::off317) = %{version}
Provides:       perl(Date::Manip::Offset::off318) = %{version}
Provides:       perl(Date::Manip::Offset::off319) = %{version}
Provides:       perl(Date::Manip::Offset::off320) = %{version}
Provides:       perl(Date::Manip::Offset::off321) = %{version}
Provides:       perl(Date::Manip::Offset::off322) = %{version}
Provides:       perl(Date::Manip::Offset::off323) = %{version}
Provides:       perl(Date::Manip::Offset::off324) = %{version}
Provides:       perl(Date::Manip::Offset::off325) = %{version}
Provides:       perl(Date::Manip::Offset::off326) = %{version}
Provides:       perl(Date::Manip::Offset::off327) = %{version}
Provides:       perl(Date::Manip::Offset::off328) = %{version}
Provides:       perl(Date::Manip::Offset::off329) = %{version}
Provides:       perl(Date::Manip::Offset::off330) = %{version}
Provides:       perl(Date::Manip::Offset::off331) = %{version}
Provides:       perl(Date::Manip::Offset::off332) = %{version}
Provides:       perl(Date::Manip::Offset::off333) = %{version}
Provides:       perl(Date::Manip::Offset::off334) = %{version}
Provides:       perl(Date::Manip::Offset::off335) = %{version}
Provides:       perl(Date::Manip::Offset::off336) = %{version}
Provides:       perl(Date::Manip::Offset::off337) = %{version}
Provides:       perl(Date::Manip::Offset::off338) = %{version}
Provides:       perl(Date::Manip::Offset::off339) = %{version}
Provides:       perl(Date::Manip::Offset::off340) = %{version}
Provides:       perl(Date::Manip::Offset::off341) = %{version}
Provides:       perl(Date::Manip::Offset::off342) = %{version}
Provides:       perl(Date::Manip::Offset::off343) = %{version}
Provides:       perl(Date::Manip::Offset::off344) = %{version}
Provides:       perl(Date::Manip::Offset::off345) = %{version}
Provides:       perl(Date::Manip::Offset::off346) = %{version}
Provides:       perl(Date::Manip::Offset::off347) = %{version}
Provides:       perl(Date::Manip::Offset::off348) = %{version}
Provides:       perl(Date::Manip::Offset::off349) = %{version}
Provides:       perl(Date::Manip::Offset::off350) = %{version}
Provides:       perl(Date::Manip::Offset::off351) = %{version}
Provides:       perl(Date::Manip::Offset::off352) = %{version}
Provides:       perl(Date::Manip::Offset::off353) = %{version}
Provides:       perl(Date::Manip::Offset::off354) = %{version}
Provides:       perl(Date::Manip::Offset::off355) = %{version}
Provides:       perl(Date::Manip::Offset::off356) = %{version}
Provides:       perl(Date::Manip::Offset::off357) = %{version}
Provides:       perl(Date::Manip::Offset::off358) = %{version}
Provides:       perl(Date::Manip::Offset::off359) = %{version}
Provides:       perl(Date::Manip::Offset::off360) = %{version}
Provides:       perl(Date::Manip::Offset::off361) = %{version}
Provides:       perl(Date::Manip::Offset::off362) = %{version}
Provides:       perl(Date::Manip::Offset::off363) = %{version}
Provides:       perl(Date::Manip::Offset::off364) = %{version}
Provides:       perl(Date::Manip::Offset::off365) = %{version}
Provides:       perl(Date::Manip::Offset::off366) = %{version}
Provides:       perl(Date::Manip::Offset::off367) = %{version}
Provides:       perl(Date::Manip::Offset::off368) = %{version}
Provides:       perl(Date::Manip::Offset::off369) = %{version}
Provides:       perl(Date::Manip::Offset::off370) = %{version}
Provides:       perl(Date::Manip::Offset::off371) = %{version}
Provides:       perl(Date::Manip::Offset::off372) = %{version}
Provides:       perl(Date::Manip::Offset::off373) = %{version}
Provides:       perl(Date::Manip::Offset::off374) = %{version}
Provides:       perl(Date::Manip::Offset::off375) = %{version}
Provides:       perl(Date::Manip::Offset::off376) = %{version}
Provides:       perl(Date::Manip::Offset::off377) = %{version}
Provides:       perl(Date::Manip::Offset::off378) = %{version}
Provides:       perl(Date::Manip::Offset::off379) = %{version}
Provides:       perl(Date::Manip::Offset::off380) = %{version}
Provides:       perl(Date::Manip::Offset::off381) = %{version}
Provides:       perl(Date::Manip::Offset::off382) = %{version}
Provides:       perl(Date::Manip::Offset::off383) = %{version}
Provides:       perl(Date::Manip::Offset::off384) = %{version}
Provides:       perl(Date::Manip::Offset::off385) = %{version}
Provides:       perl(Date::Manip::Offset::off386) = %{version}
Provides:       perl(Date::Manip::Offset::off387) = %{version}
Provides:       perl(Date::Manip::Offset::off388) = %{version}
Provides:       perl(Date::Manip::Offset::off389) = %{version}
Provides:       perl(Date::Manip::Offset::off390) = %{version}
Provides:       perl(Date::Manip::Offset::off391) = %{version}
Provides:       perl(Date::Manip::Offset::off392) = %{version}
Provides:       perl(Date::Manip::Offset::off393) = %{version}
Provides:       perl(Date::Manip::Offset::off394) = %{version}
Provides:       perl(Date::Manip::Offset::off395) = %{version}
Provides:       perl(Date::Manip::Offset::off396) = %{version}
Provides:       perl(Date::Manip::Offset::off397) = %{version}
Provides:       perl(Date::Manip::Offset::off398) = %{version}
Provides:       perl(Date::Manip::Offset::off399) = %{version}
Provides:       perl(Date::Manip::Offset::off400) = %{version}
Provides:       perl(Date::Manip::Offset::off401) = %{version}
Provides:       perl(Date::Manip::Offset::off402) = %{version}
Provides:       perl(Date::Manip::Offset::off403) = %{version}
Provides:       perl(Date::Manip::Offset::off404) = %{version}
Provides:       perl(Date::Manip::Offset::off405) = %{version}
Provides:       perl(Date::Manip::Offset::off406) = %{version}
Provides:       perl(Date::Manip::Recur) = %{version}
Provides:       perl(Date::Manip::TZ) = %{version}
Provides:       perl(Date::Manip::TZ::a00) = %{version}
Provides:       perl(Date::Manip::TZ::afabid00) = %{version}
Provides:       perl(Date::Manip::TZ::afalgi00) = %{version}
Provides:       perl(Date::Manip::TZ::afbiss00) = %{version}
Provides:       perl(Date::Manip::TZ::afcair00) = %{version}
Provides:       perl(Date::Manip::TZ::afcasa00) = %{version}
Provides:       perl(Date::Manip::TZ::afceut00) = %{version}
Provides:       perl(Date::Manip::TZ::afel_a00) = %{version}
Provides:       perl(Date::Manip::TZ::afjoha00) = %{version}
Provides:       perl(Date::Manip::TZ::afjuba00) = %{version}
Provides:       perl(Date::Manip::TZ::afkhar00) = %{version}
Provides:       perl(Date::Manip::TZ::aflago00) = %{version}
Provides:       perl(Date::Manip::TZ::afmapu00) = %{version}
Provides:       perl(Date::Manip::TZ::afmonr00) = %{version}
Provides:       perl(Date::Manip::TZ::afnair00) = %{version}
Provides:       perl(Date::Manip::TZ::afndja00) = %{version}
Provides:       perl(Date::Manip::TZ::afsao_00) = %{version}
Provides:       perl(Date::Manip::TZ::aftrip00) = %{version}
Provides:       perl(Date::Manip::TZ::aftuni00) = %{version}
Provides:       perl(Date::Manip::TZ::afwind00) = %{version}
Provides:       perl(Date::Manip::TZ::amadak00) = %{version}
Provides:       perl(Date::Manip::TZ::amanch00) = %{version}
Provides:       perl(Date::Manip::TZ::amarag00) = %{version}
Provides:       perl(Date::Manip::TZ::amasun00) = %{version}
Provides:       perl(Date::Manip::TZ::ambahi00) = %{version}
Provides:       perl(Date::Manip::TZ::ambahi01) = %{version}
Provides:       perl(Date::Manip::TZ::ambarb00) = %{version}
Provides:       perl(Date::Manip::TZ::ambele00) = %{version}
Provides:       perl(Date::Manip::TZ::ambeli00) = %{version}
Provides:       perl(Date::Manip::TZ::ambeul00) = %{version}
Provides:       perl(Date::Manip::TZ::amboa_00) = %{version}
Provides:       perl(Date::Manip::TZ::ambogo00) = %{version}
Provides:       perl(Date::Manip::TZ::ambois00) = %{version}
Provides:       perl(Date::Manip::TZ::ambuen00) = %{version}
Provides:       perl(Date::Manip::TZ::amcamb00) = %{version}
Provides:       perl(Date::Manip::TZ::amcamp00) = %{version}
Provides:       perl(Date::Manip::TZ::amcanc00) = %{version}
Provides:       perl(Date::Manip::TZ::amcara00) = %{version}
Provides:       perl(Date::Manip::TZ::amcata00) = %{version}
Provides:       perl(Date::Manip::TZ::amcaye00) = %{version}
Provides:       perl(Date::Manip::TZ::amcent00) = %{version}
Provides:       perl(Date::Manip::TZ::amchic00) = %{version}
Provides:       perl(Date::Manip::TZ::amchih00) = %{version}
Provides:       perl(Date::Manip::TZ::amciud00) = %{version}
Provides:       perl(Date::Manip::TZ::amcord00) = %{version}
Provides:       perl(Date::Manip::TZ::amcost00) = %{version}
Provides:       perl(Date::Manip::TZ::amcuia00) = %{version}
Provides:       perl(Date::Manip::TZ::amdanm00) = %{version}
Provides:       perl(Date::Manip::TZ::amdaws00) = %{version}
Provides:       perl(Date::Manip::TZ::amdaws01) = %{version}
Provides:       perl(Date::Manip::TZ::amdenv00) = %{version}
Provides:       perl(Date::Manip::TZ::amdetr00) = %{version}
Provides:       perl(Date::Manip::TZ::amedmo00) = %{version}
Provides:       perl(Date::Manip::TZ::ameiru00) = %{version}
Provides:       perl(Date::Manip::TZ::amel_s00) = %{version}
Provides:       perl(Date::Manip::TZ::amfort00) = %{version}
Provides:       perl(Date::Manip::TZ::amfort01) = %{version}
Provides:       perl(Date::Manip::TZ::amglac00) = %{version}
Provides:       perl(Date::Manip::TZ::amgoos00) = %{version}
Provides:       perl(Date::Manip::TZ::amgran00) = %{version}
Provides:       perl(Date::Manip::TZ::amguat00) = %{version}
Provides:       perl(Date::Manip::TZ::amguay00) = %{version}
Provides:       perl(Date::Manip::TZ::amguya00) = %{version}
Provides:       perl(Date::Manip::TZ::amhali00) = %{version}
Provides:       perl(Date::Manip::TZ::amhava00) = %{version}
Provides:       perl(Date::Manip::TZ::amherm00) = %{version}
Provides:       perl(Date::Manip::TZ::amindi00) = %{version}
Provides:       perl(Date::Manip::TZ::aminuv00) = %{version}
Provides:       perl(Date::Manip::TZ::amiqal00) = %{version}
Provides:       perl(Date::Manip::TZ::amjama00) = %{version}
Provides:       perl(Date::Manip::TZ::amjuju00) = %{version}
Provides:       perl(Date::Manip::TZ::amjune00) = %{version}
Provides:       perl(Date::Manip::TZ::amknox00) = %{version}
Provides:       perl(Date::Manip::TZ::amla_p00) = %{version}
Provides:       perl(Date::Manip::TZ::amla_r00) = %{version}
Provides:       perl(Date::Manip::TZ::amlima00) = %{version}
Provides:       perl(Date::Manip::TZ::amlos_00) = %{version}
Provides:       perl(Date::Manip::TZ::amloui00) = %{version}
Provides:       perl(Date::Manip::TZ::ammace00) = %{version}
Provides:       perl(Date::Manip::TZ::ammana00) = %{version}
Provides:       perl(Date::Manip::TZ::ammana01) = %{version}
Provides:       perl(Date::Manip::TZ::ammare00) = %{version}
Provides:       perl(Date::Manip::TZ::ammart00) = %{version}
Provides:       perl(Date::Manip::TZ::ammata00) = %{version}
Provides:       perl(Date::Manip::TZ::ammaza00) = %{version}
Provides:       perl(Date::Manip::TZ::ammend00) = %{version}
Provides:       perl(Date::Manip::TZ::ammeno00) = %{version}
Provides:       perl(Date::Manip::TZ::ammeri00) = %{version}
Provides:       perl(Date::Manip::TZ::ammetl00) = %{version}
Provides:       perl(Date::Manip::TZ::ammexi00) = %{version}
Provides:       perl(Date::Manip::TZ::ammiqu00) = %{version}
Provides:       perl(Date::Manip::TZ::ammonc00) = %{version}
Provides:       perl(Date::Manip::TZ::ammont00) = %{version}
Provides:       perl(Date::Manip::TZ::ammont01) = %{version}
Provides:       perl(Date::Manip::TZ::ammont02) = %{version}
Provides:       perl(Date::Manip::TZ::amnew_00) = %{version}
Provides:       perl(Date::Manip::TZ::amnew_01) = %{version}
Provides:       perl(Date::Manip::TZ::amnome00) = %{version}
Provides:       perl(Date::Manip::TZ::amnoro00) = %{version}
Provides:       perl(Date::Manip::TZ::amnuuk00) = %{version}
Provides:       perl(Date::Manip::TZ::amojin00) = %{version}
Provides:       perl(Date::Manip::TZ::ampana00) = %{version}
Provides:       perl(Date::Manip::TZ::ampara00) = %{version}
Provides:       perl(Date::Manip::TZ::ampete00) = %{version}
Provides:       perl(Date::Manip::TZ::amphoe00) = %{version}
Provides:       perl(Date::Manip::TZ::amport00) = %{version}
Provides:       perl(Date::Manip::TZ::amport01) = %{version}
Provides:       perl(Date::Manip::TZ::ampuer00) = %{version}
Provides:       perl(Date::Manip::TZ::ampunt00) = %{version}
Provides:       perl(Date::Manip::TZ::amrank00) = %{version}
Provides:       perl(Date::Manip::TZ::amreci00) = %{version}
Provides:       perl(Date::Manip::TZ::amregi00) = %{version}
Provides:       perl(Date::Manip::TZ::amreso00) = %{version}
Provides:       perl(Date::Manip::TZ::amrio_00) = %{version}
Provides:       perl(Date::Manip::TZ::amrio_01) = %{version}
Provides:       perl(Date::Manip::TZ::amsalt00) = %{version}
Provides:       perl(Date::Manip::TZ::amsan_00) = %{version}
Provides:       perl(Date::Manip::TZ::amsan_01) = %{version}
Provides:       perl(Date::Manip::TZ::amsant00) = %{version}
Provides:       perl(Date::Manip::TZ::amsant01) = %{version}
Provides:       perl(Date::Manip::TZ::amsant02) = %{version}
Provides:       perl(Date::Manip::TZ::amsao_00) = %{version}
Provides:       perl(Date::Manip::TZ::amscor00) = %{version}
Provides:       perl(Date::Manip::TZ::amsitk00) = %{version}
Provides:       perl(Date::Manip::TZ::amst_j00) = %{version}
Provides:       perl(Date::Manip::TZ::amswif00) = %{version}
Provides:       perl(Date::Manip::TZ::amtegu00) = %{version}
Provides:       perl(Date::Manip::TZ::amtell00) = %{version}
Provides:       perl(Date::Manip::TZ::amthul00) = %{version}
Provides:       perl(Date::Manip::TZ::amtiju00) = %{version}
Provides:       perl(Date::Manip::TZ::amtoro00) = %{version}
Provides:       perl(Date::Manip::TZ::amtucu00) = %{version}
Provides:       perl(Date::Manip::TZ::amushu00) = %{version}
Provides:       perl(Date::Manip::TZ::amvanc00) = %{version}
Provides:       perl(Date::Manip::TZ::amveva00) = %{version}
Provides:       perl(Date::Manip::TZ::amvinc00) = %{version}
Provides:       perl(Date::Manip::TZ::amwhit00) = %{version}
Provides:       perl(Date::Manip::TZ::amwina00) = %{version}
Provides:       perl(Date::Manip::TZ::amwinn00) = %{version}
Provides:       perl(Date::Manip::TZ::amyaku00) = %{version}
Provides:       perl(Date::Manip::TZ::ancase00) = %{version}
Provides:       perl(Date::Manip::TZ::andavi00) = %{version}
Provides:       perl(Date::Manip::TZ::anmacq00) = %{version}
Provides:       perl(Date::Manip::TZ::anmaws00) = %{version}
Provides:       perl(Date::Manip::TZ::anpalm00) = %{version}
Provides:       perl(Date::Manip::TZ::anroth00) = %{version}
Provides:       perl(Date::Manip::TZ::antrol00) = %{version}
Provides:       perl(Date::Manip::TZ::anvost00) = %{version}
Provides:       perl(Date::Manip::TZ::asalma00) = %{version}
Provides:       perl(Date::Manip::TZ::asamma00) = %{version}
Provides:       perl(Date::Manip::TZ::asanad00) = %{version}
Provides:       perl(Date::Manip::TZ::asaqta00) = %{version}
Provides:       perl(Date::Manip::TZ::asaqto00) = %{version}
Provides:       perl(Date::Manip::TZ::asashg00) = %{version}
Provides:       perl(Date::Manip::TZ::asatyr00) = %{version}
Provides:       perl(Date::Manip::TZ::asbagh00) = %{version}
Provides:       perl(Date::Manip::TZ::asbaku00) = %{version}
Provides:       perl(Date::Manip::TZ::asbang00) = %{version}
Provides:       perl(Date::Manip::TZ::asbarn00) = %{version}
Provides:       perl(Date::Manip::TZ::asbeir00) = %{version}
Provides:       perl(Date::Manip::TZ::asbish00) = %{version}
Provides:       perl(Date::Manip::TZ::aschit00) = %{version}
Provides:       perl(Date::Manip::TZ::ascolo00) = %{version}
Provides:       perl(Date::Manip::TZ::asdama00) = %{version}
Provides:       perl(Date::Manip::TZ::asdhak00) = %{version}
Provides:       perl(Date::Manip::TZ::asdili00) = %{version}
Provides:       perl(Date::Manip::TZ::asduba00) = %{version}
Provides:       perl(Date::Manip::TZ::asdush00) = %{version}
Provides:       perl(Date::Manip::TZ::asfama00) = %{version}
Provides:       perl(Date::Manip::TZ::asgaza00) = %{version}
Provides:       perl(Date::Manip::TZ::ashebr00) = %{version}
Provides:       perl(Date::Manip::TZ::asho_c00) = %{version}
Provides:       perl(Date::Manip::TZ::ashong00) = %{version}
Provides:       perl(Date::Manip::TZ::ashovd00) = %{version}
Provides:       perl(Date::Manip::TZ::asirku00) = %{version}
Provides:       perl(Date::Manip::TZ::asjaka00) = %{version}
Provides:       perl(Date::Manip::TZ::asjaya00) = %{version}
Provides:       perl(Date::Manip::TZ::asjeru00) = %{version}
Provides:       perl(Date::Manip::TZ::askabu00) = %{version}
Provides:       perl(Date::Manip::TZ::askamc00) = %{version}
Provides:       perl(Date::Manip::TZ::askara00) = %{version}
Provides:       perl(Date::Manip::TZ::askath00) = %{version}
Provides:       perl(Date::Manip::TZ::askhan00) = %{version}
Provides:       perl(Date::Manip::TZ::askolk00) = %{version}
Provides:       perl(Date::Manip::TZ::askras00) = %{version}
Provides:       perl(Date::Manip::TZ::askuch00) = %{version}
Provides:       perl(Date::Manip::TZ::asmaca00) = %{version}
Provides:       perl(Date::Manip::TZ::asmaga00) = %{version}
Provides:       perl(Date::Manip::TZ::asmaka00) = %{version}
Provides:       perl(Date::Manip::TZ::asmani00) = %{version}
Provides:       perl(Date::Manip::TZ::asnico00) = %{version}
Provides:       perl(Date::Manip::TZ::asnovo00) = %{version}
Provides:       perl(Date::Manip::TZ::asnovo01) = %{version}
Provides:       perl(Date::Manip::TZ::asomsk00) = %{version}
Provides:       perl(Date::Manip::TZ::asoral00) = %{version}
Provides:       perl(Date::Manip::TZ::aspont00) = %{version}
Provides:       perl(Date::Manip::TZ::aspyon00) = %{version}
Provides:       perl(Date::Manip::TZ::asqata00) = %{version}
Provides:       perl(Date::Manip::TZ::asqost00) = %{version}
Provides:       perl(Date::Manip::TZ::asqyzy00) = %{version}
Provides:       perl(Date::Manip::TZ::asriya00) = %{version}
Provides:       perl(Date::Manip::TZ::assakh00) = %{version}
Provides:       perl(Date::Manip::TZ::assama00) = %{version}
Provides:       perl(Date::Manip::TZ::asseou00) = %{version}
Provides:       perl(Date::Manip::TZ::asshan00) = %{version}
Provides:       perl(Date::Manip::TZ::assing00) = %{version}
Provides:       perl(Date::Manip::TZ::assred00) = %{version}
Provides:       perl(Date::Manip::TZ::astaip00) = %{version}
Provides:       perl(Date::Manip::TZ::astash00) = %{version}
Provides:       perl(Date::Manip::TZ::astbil00) = %{version}
Provides:       perl(Date::Manip::TZ::astehr00) = %{version}
Provides:       perl(Date::Manip::TZ::asthim00) = %{version}
Provides:       perl(Date::Manip::TZ::astoky00) = %{version}
Provides:       perl(Date::Manip::TZ::astoms00) = %{version}
Provides:       perl(Date::Manip::TZ::asulaa00) = %{version}
Provides:       perl(Date::Manip::TZ::asurum00) = %{version}
Provides:       perl(Date::Manip::TZ::asustm00) = %{version}
Provides:       perl(Date::Manip::TZ::asvlad00) = %{version}
Provides:       perl(Date::Manip::TZ::asyaku00) = %{version}
Provides:       perl(Date::Manip::TZ::asyang00) = %{version}
Provides:       perl(Date::Manip::TZ::asyeka00) = %{version}
Provides:       perl(Date::Manip::TZ::asyere00) = %{version}
Provides:       perl(Date::Manip::TZ::atazor00) = %{version}
Provides:       perl(Date::Manip::TZ::atberm00) = %{version}
Provides:       perl(Date::Manip::TZ::atcana00) = %{version}
Provides:       perl(Date::Manip::TZ::atcape00) = %{version}
Provides:       perl(Date::Manip::TZ::atfaro00) = %{version}
Provides:       perl(Date::Manip::TZ::atmade00) = %{version}
Provides:       perl(Date::Manip::TZ::atsout00) = %{version}
Provides:       perl(Date::Manip::TZ::atstan00) = %{version}
Provides:       perl(Date::Manip::TZ::auadel00) = %{version}
Provides:       perl(Date::Manip::TZ::aubris00) = %{version}
Provides:       perl(Date::Manip::TZ::aubrok00) = %{version}
Provides:       perl(Date::Manip::TZ::audarw00) = %{version}
Provides:       perl(Date::Manip::TZ::aueucl00) = %{version}
Provides:       perl(Date::Manip::TZ::auhoba00) = %{version}
Provides:       perl(Date::Manip::TZ::aulind00) = %{version}
Provides:       perl(Date::Manip::TZ::aulord00) = %{version}
Provides:       perl(Date::Manip::TZ::aumelb00) = %{version}
Provides:       perl(Date::Manip::TZ::aupert00) = %{version}
Provides:       perl(Date::Manip::TZ::ausydn00) = %{version}
Provides:       perl(Date::Manip::TZ::b00) = %{version}
Provides:       perl(Date::Manip::TZ::c00) = %{version}
Provides:       perl(Date::Manip::TZ::d00) = %{version}
Provides:       perl(Date::Manip::TZ::e00) = %{version}
Provides:       perl(Date::Manip::TZ::etgmt00) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm00) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm01) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm02) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm03) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm04) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm05) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm06) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm07) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm08) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm09) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm10) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm11) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm12) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtm13) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp00) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp01) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp02) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp03) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp04) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp05) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp06) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp07) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp08) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp09) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp10) = %{version}
Provides:       perl(Date::Manip::TZ::etgmtp11) = %{version}
Provides:       perl(Date::Manip::TZ::etutc00) = %{version}
Provides:       perl(Date::Manip::TZ::euando00) = %{version}
Provides:       perl(Date::Manip::TZ::euastr00) = %{version}
Provides:       perl(Date::Manip::TZ::euathe00) = %{version}
Provides:       perl(Date::Manip::TZ::eubelg00) = %{version}
Provides:       perl(Date::Manip::TZ::euberl00) = %{version}
Provides:       perl(Date::Manip::TZ::eubrus00) = %{version}
Provides:       perl(Date::Manip::TZ::eubuch00) = %{version}
Provides:       perl(Date::Manip::TZ::eubuda00) = %{version}
Provides:       perl(Date::Manip::TZ::euchis00) = %{version}
Provides:       perl(Date::Manip::TZ::eudubl00) = %{version}
Provides:       perl(Date::Manip::TZ::eugibr00) = %{version}
Provides:       perl(Date::Manip::TZ::euhels00) = %{version}
Provides:       perl(Date::Manip::TZ::euista00) = %{version}
Provides:       perl(Date::Manip::TZ::eukali00) = %{version}
Provides:       perl(Date::Manip::TZ::eukiro00) = %{version}
Provides:       perl(Date::Manip::TZ::eukyiv00) = %{version}
Provides:       perl(Date::Manip::TZ::eulisb00) = %{version}
Provides:       perl(Date::Manip::TZ::eulond00) = %{version}
Provides:       perl(Date::Manip::TZ::eumadr00) = %{version}
Provides:       perl(Date::Manip::TZ::eumalt00) = %{version}
Provides:       perl(Date::Manip::TZ::eumins00) = %{version}
Provides:       perl(Date::Manip::TZ::eumosc00) = %{version}
Provides:       perl(Date::Manip::TZ::eupari00) = %{version}
Provides:       perl(Date::Manip::TZ::euprag00) = %{version}
Provides:       perl(Date::Manip::TZ::euriga00) = %{version}
Provides:       perl(Date::Manip::TZ::eurome00) = %{version}
Provides:       perl(Date::Manip::TZ::eusama00) = %{version}
Provides:       perl(Date::Manip::TZ::eusara00) = %{version}
Provides:       perl(Date::Manip::TZ::eusimf00) = %{version}
Provides:       perl(Date::Manip::TZ::eusofi00) = %{version}
Provides:       perl(Date::Manip::TZ::eutall00) = %{version}
Provides:       perl(Date::Manip::TZ::eutira00) = %{version}
Provides:       perl(Date::Manip::TZ::euulya00) = %{version}
Provides:       perl(Date::Manip::TZ::euvien00) = %{version}
Provides:       perl(Date::Manip::TZ::euviln00) = %{version}
Provides:       perl(Date::Manip::TZ::euvolg00) = %{version}
Provides:       perl(Date::Manip::TZ::euwars00) = %{version}
Provides:       perl(Date::Manip::TZ::euzuri00) = %{version}
Provides:       perl(Date::Manip::TZ::f00) = %{version}
Provides:       perl(Date::Manip::TZ::g00) = %{version}
Provides:       perl(Date::Manip::TZ::h00) = %{version}
Provides:       perl(Date::Manip::TZ::i00) = %{version}
Provides:       perl(Date::Manip::TZ::inchag00) = %{version}
Provides:       perl(Date::Manip::TZ::inmald00) = %{version}
Provides:       perl(Date::Manip::TZ::inmaur00) = %{version}
Provides:       perl(Date::Manip::TZ::k00) = %{version}
Provides:       perl(Date::Manip::TZ::l00) = %{version}
Provides:       perl(Date::Manip::TZ::m00) = %{version}
Provides:       perl(Date::Manip::TZ::n00) = %{version}
Provides:       perl(Date::Manip::TZ::o00) = %{version}
Provides:       perl(Date::Manip::TZ::p00) = %{version}
Provides:       perl(Date::Manip::TZ::paapia00) = %{version}
Provides:       perl(Date::Manip::TZ::paauck00) = %{version}
Provides:       perl(Date::Manip::TZ::paboug00) = %{version}
Provides:       perl(Date::Manip::TZ::pachat00) = %{version}
Provides:       perl(Date::Manip::TZ::paeast00) = %{version}
Provides:       perl(Date::Manip::TZ::paefat00) = %{version}
Provides:       perl(Date::Manip::TZ::pafaka00) = %{version}
Provides:       perl(Date::Manip::TZ::pafiji00) = %{version}
Provides:       perl(Date::Manip::TZ::pagala00) = %{version}
Provides:       perl(Date::Manip::TZ::pagamb00) = %{version}
Provides:       perl(Date::Manip::TZ::paguad00) = %{version}
Provides:       perl(Date::Manip::TZ::paguam00) = %{version}
Provides:       perl(Date::Manip::TZ::pahono00) = %{version}
Provides:       perl(Date::Manip::TZ::pakant00) = %{version}
Provides:       perl(Date::Manip::TZ::pakiri00) = %{version}
Provides:       perl(Date::Manip::TZ::pakosr00) = %{version}
Provides:       perl(Date::Manip::TZ::pakwaj00) = %{version}
Provides:       perl(Date::Manip::TZ::pamarq00) = %{version}
Provides:       perl(Date::Manip::TZ::panaur00) = %{version}
Provides:       perl(Date::Manip::TZ::paniue00) = %{version}
Provides:       perl(Date::Manip::TZ::panorf00) = %{version}
Provides:       perl(Date::Manip::TZ::panoum00) = %{version}
Provides:       perl(Date::Manip::TZ::papago00) = %{version}
Provides:       perl(Date::Manip::TZ::papala00) = %{version}
Provides:       perl(Date::Manip::TZ::papitc00) = %{version}
Provides:       perl(Date::Manip::TZ::paport00) = %{version}
Provides:       perl(Date::Manip::TZ::pararo00) = %{version}
Provides:       perl(Date::Manip::TZ::patahi00) = %{version}
Provides:       perl(Date::Manip::TZ::patara00) = %{version}
Provides:       perl(Date::Manip::TZ::patong00) = %{version}
Provides:       perl(Date::Manip::TZ::q00) = %{version}
Provides:       perl(Date::Manip::TZ::r00) = %{version}
Provides:       perl(Date::Manip::TZ::s00) = %{version}
Provides:       perl(Date::Manip::TZ::t00) = %{version}
Provides:       perl(Date::Manip::TZ::u00) = %{version}
Provides:       perl(Date::Manip::TZ::ut00) = %{version}
Provides:       perl(Date::Manip::TZ::v00) = %{version}
Provides:       perl(Date::Manip::TZ::w00) = %{version}
Provides:       perl(Date::Manip::TZ::x00) = %{version}
Provides:       perl(Date::Manip::TZ::y00) = %{version}
Provides:       perl(Date::Manip::TZ::z00) = %{version}
Provides:       perl(Date::Manip::TZ_Base) = %{version}
Provides:       perl(Date::Manip::TZdata) = %{version}
Provides:       perl(Date::Manip::Zones) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Date::Manip is a series of modules designed to make any common date/time
operation easy to do. Operations such as comparing two times, determining a
date a given amount of time from another, or parsing international times
are all easily done. It deals with time as it is used in the Gregorian
calendar (the one currently in use) with full support for time changes due
to daylight saving time.

From the very beginning, the main focus of Date::Manip has been to be able
to do ANY desired date/time operation easily. Many other modules exist
which may do a subset of these operations quicker or more efficiently, but
no other module can do all of the operations available in Date::Manip.

Date::Manip has functionality to work with several fundamental types of
data.

* *dates*

The word date is used extensively here and is somewhat misleading. In
Date::Manip, a date consists of three pieces of information: a calendar
date (year, month, day), a time of day (hour, minute, second), and time
zone information. Calendar dates and times are fully handled. Time zones
are handled as well, but depending on how you use Date::Manip, there may be
some limitations as discussed below.

* *delta*

A delta is an amount of time (i.e. the amount of time between two different
dates). Think of it as the duration of an event or the amount of time
between two dates.

A delta refers only to an amount of time. It includes no information about
a starting or ending date/time. Most people will think of a delta as an
amount of time, but the term 'time' is already used so much in this module
that I didn't want to use it here in order to avoid confusion.

* *recurrence*

A recurring event is something which occurs on a regular recurring basis.

* *holidays* and *events*

Holidays and events are basically named dates or recurrences.

Among other things, Date::Manip allow you to:

* ***

Enter a date in practically any format you choose.

* ***

Compare two dates, entered in widely different formats to determine which
is earlier.

* ***

Extract any information you want from a date using a format string similar
to the Unix date command.

* ***

Determine the amount of time between two dates, or add an amount of time (a
delta) to a date to get a second date.

* ***

Work with dates using international formats (foreign month names, 12/10/95
referring to October rather than December, etc.).

* ***

Convert dates from one timezone to another.

* ***

To find a list of dates where a recurring event happens.

Each of these tasks is trivial (one or two lines at most) with this
package.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples README README.first
%license LICENSE

%changelog
