/* Setup if we need nm-applet? */
#include "e_wizard.h"

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define GNOME_KEYRING_PATH "/etc/xdg/autostart/gnome-keyring-secrets.desktop"
#define NM_APPLET_PATH     "/etc/xdg/autostart/nm-applet.desktop"

/*

E_API int
wizard_page_init(E_Wizard_Page *pg EINA_UNUSED, Eina_Bool *need_xdg_desktops EINA_UNUSED, Eina_Bool *need_xdg_icons EINA_UNUSED)
{
   return 1;
}

E_API int
wizard_page_shutdown(E_Wizard_Page *pg EINA_UNUSED)
{
   return 1;
}
*/

E_API int
wizard_page_show(E_Wizard_Page *pg)
{
  // copyed from e_start_main.c
  char buf[16384], * home;
  FILE *fp;

  home = getenv("HOME");

  if (home && (0 == access(GNOME_KEYRING_PATH, F_OK)) && (0 == access(NM_APPLET_PATH, F_OK)))
  {
    snprintf(buf, sizeof(buf), "%s/.e/e/applications/startup/.order", home);

    printf("%s\n", buf);

    fp=fopen(buf, "a+");
    fprintf(fp, "%s\n%s\n", GNOME_KEYRING_PATH, NM_APPLET_PATH);
    fclose(fp);
  }

   return 0; /* 1 == show ui, and wait for user, 0 == just continue */
}

/*
E_API int
wizard_page_hide(E_Wizard_Page *pg EINA_UNUSED)
{
   return 1;
}

E_API int
wizard_page_apply(E_Wizard_Page *pg EINA_UNUSED)
{
   return 1;
}
*/
