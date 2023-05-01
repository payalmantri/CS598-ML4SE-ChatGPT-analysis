def _apply_perspective(coords:FlowField, coeffs:Points)->FlowField:
    "Transform `coords` with `coeffs`."
    size = coords.flow.size()
    #compress all the dims expect the last one ang adds ones, coords become N * 3
    coords.flow = coords.flow.view(-1,2)
    #Transform the coeffs in a 3*3 matrix with a 1 at the bottom left
    coeffs = torch.cat([coeffs, FloatTensor([1])]).view(3,3)
    coords.flow = torch.addmm(coeffs[:,2], coords.flow, coeffs[:,:2].t())
    coords.flow.mul_(1/coords.flow[:,2].unsqueeze(1))
    coords.flow = coords.flow[:,:2].view(size)
    return coords