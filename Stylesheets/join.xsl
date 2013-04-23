<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<!-- Thanks to: http://stackoverflow.com/questions/798269/xslt-concat-string-remove-last-comma#798572 -->
<xsl:template name="join">
    <xsl:param name="list" />
    <xsl:param name="separator"/>

    <xsl:for-each select="$list">
        <xsl:value-of select="." />
        <xsl:if test="position() != last()">
            <xsl:value-of select="$separator" />
        </xsl:if>
    </xsl:for-each>
</xsl:template>
</xsl:stylesheet>
