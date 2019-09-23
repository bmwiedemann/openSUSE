# ------------------------------------------------------------------------------
# Copyright (c) 2013 Novell, Inc. All Rights Reserved.
#
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
#

#
# File:	clients/virt-install.ycp
# Package:	Installation of a virtual machine
# Summary:	Main VM installation YaST frontend for python based virt-install
# Authors:	Charles E. Arnold <carnold@suse.com>
#
# $Id$

module Yast
  class VirtinstallClient < Client
    def main
      textdomain "virt-install"

      Yast.import "UI"
      Yast.import "Popup"
      Yast.import "String"
      Yast.import "Arch"

      #===================================================================
      # Start virt-install (GUI) or vm-install if Text mode (commandline)
      #-------------------------------------------------------------------
      status = 0
      @details = {}

      Builtins.y2milestone("START HERE.")
      if UI.TextMode()
        Builtins.y2milestone("Running virt-install in text mode is not supported. Running vm-install instead in command line mode.")
        status = UI.RunInTerminal("/usr/bin/vm-install")
      else
        Builtins.y2milestone("Launching virt-manager to run virt-install in GUI mode.")
        if Arch.is_xen == false
          details = Convert.to_map(SCR.Execute(path(".target.bash_output"), "/usr/bin/virt-manager --connect=qemu:///system --show-domain-creator"))
        else
          details = Convert.to_map(SCR.Execute(path(".target.bash_output"), "/usr/bin/virt-manager --connect=xen:/// --show-domain-creator"))
        end
        status = Ops.get_integer(details, "exit", 0)
      end

      Builtins.y2milestone("virt-install finished with exit code: <%1>", status)
      if status == 0
        return :next
      else
        if Builtins.size(Ops.get_string(details, "stderr", "")) > 0
          Popup.ErrorDetails(_("Failed to start virt-install"), Convert.to_string(details, "stderr", ""))
        else
          Popup.Error(_("Failed to start virt-install"))
        end
      end

      nil
    end
  end
end

Yast::VirtinstallClient.new.main
