# encoding: utf-8

# ------------------------------------------------------------------------------
# Copyright (c) 2019 SUSE Inc., Inc. All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of version 2 of the GNU General Public License as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, contact Novell, Inc.
#
# To contact Novell about this file by physical or electronic mail, you may find
# current contact information at www.novell.com.
# ------------------------------------------------------------------------------

require "yast2/target_file"
require "etc"

module Yast
  class FirstbootWriteWSLClient < Client
    def main

      return :back if GetInstArgs.going_back

      @users = UsersSimple.GetUsers()
      unless @users.empty?
        @uid = Etc.getpwnam(@users[0]['uid']).uid
        Yast::TargetFile.write("/run/wsl_firstboot_uid", @uid)
      end

      # systemd-machine-id-setup is smart enough to only populate
      # /etc/machine-id when empty or missing
      SCR.Execute(path('.target.bash'), '/usr/bin/systemd-machine-id-setup')

      :next 

      #EOF
    end
  end
end

Yast::FirstbootWriteWSLClient.new.main
