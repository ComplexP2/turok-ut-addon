
// =============
// VERTEX SHADER
// =============

#ifdef SHADER_VERTEX
#include "progs/globals_vertex.inc"

//----------------------------------------------------
// input
begin_input(inVertex)
    var_attrib(ATTRIB_POSITION, vec3);
    var_attrib(ATTRIB_TEXCOORD, vec2);
    var_attrib(ATTRIB_COLOR, vec4);
end_input

//----------------------------------------------------
// output
begin_output(outVertex)
    def_var_outPosition(position)
    def_var_out(vec2, out_texcoord, TEXCOORD0)
    def_var_out(vec4, out_color,    COLOR0)
end_output

//uniform float uFac;

//----------------------------------------------------
shader_main(outVertex, inVertex, input)
{
    declareOutVar(outVertex, output)

    vec4 vertex                         = vec4(inVarAttrib(ATTRIB_POSITION, input), 1.0);
    //outVarPosition(output, position)    = mul(uProjectionMatrix, mul(uModelViewMatrix, vertex));
    vec4 vert = vertex; //mul(inverseViewMatrix, mul(uModelViewMatrix, vertex));
    float fac = 1.0 / 439.0;
    //float fac = 1.0/uFac;
    outVarPosition(output, position)    = vec4(vert[0]*fac, vert[1]*fac, -1.0, 1.0);
    outVar(output, out_texcoord)        = inVarAttrib(ATTRIB_TEXCOORD, input);
    outVar(output, out_color)           = inVarAttrib(ATTRIB_COLOR, input);
    
    outReturn(output)
}

#endif



// ===============
// FRAGMENT SHADER
// ===============

#ifdef SHADER_PIXEL
#include "progs/globals_fragment.inc"

//----------------------------------------------------
// input
begin_input(outVertex)
    def_var_position(position)
    def_var_in(vec2, out_texcoord, TEXCOORD0)
    def_var_in(vec4, out_color,    COLOR0)
end_input

//----------------------------------------------------
// output
begin_output(outPixel)
    def_var_fragment(fragment)
end_output

//----------------------------------------------------
shader_main(outPixel, outVertex, input)
{
    declareOutVar(outPixel, output)
    
    //outVarFragment(output, fragment) = sample_texture(0, inVar(input, out_texcoord)) * inVar(input, out_color);
    //outVarFragment(output, fragment) = vec4(1.0, 0.0, 0.0, 0.25);
    vec4 pxtex = sample_texture(0, inVar(input, out_texcoord));// * inVar(input, out_color);
    pxtex[3] = 0.25;
    outVarFragment(output, fragment) = pxtex;
    outReturn(output)
}

#endif
