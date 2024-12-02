public class PermissionController : ControllerBase
{
    private readonly IPermissionService _permissionService;

        public PermissionController(IPermissionService permissionService)
	   {
	            _permissionService = permissionService;
					        }

		    [HttpGet("{userId}")]
		        public async Task<IActionResult> GetUserPermissions(int userId)
				    {
					            var permissions = await _permissionService.GetUserPermissionsAsync(userId);
						            return Ok(permissions);
							        }

		        // Other endpoints for managing permissions (e.g., assigning, revoking)
			}
