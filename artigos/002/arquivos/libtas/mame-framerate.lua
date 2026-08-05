for k,v in pairs(manager.machine.screens) do
	local numerator = 0x3ffffffc
	local denominator = emu.attotime(0, v.refresh_attoseconds):as_ticks(numerator)
	print("\"" .. k .. "\" framerate: " .. numerator .. " / " .. denominator)
end

local bounds = manager.machine.render.ui_target.current_view.bounds
print("aspect ratio: " .. bounds.x1-bounds.x0 .. " : " .. bounds.y1-bounds.y0)
