<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
  <xsl:strip-space elements="*"/>

  <!-- Identity template to copy elements and attributes as they are -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- Add Resources element with allowLinking attribute -->
  <xsl:template match="Context">
    <xsl:copy>
      <Resources allowLinking="true" />
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
