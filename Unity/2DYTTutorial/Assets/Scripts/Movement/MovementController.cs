using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovementController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField]
    Rigidbody2D playerRigidbody2D;
    [SerializeField]
    private float maxVelocity = 5f;
    [Space(10)]

    [Header("Jumping")]
    [SerializeField]
    private Transform bottomCollisionPoint = null;
    [SerializeField]
    private LayerMask tileLayer;
    [SerializeField]
    private float jumpForce = 12f;
    [SerializeField]
    private int maxJumpCount = 1;
    [SerializeField]
    private int jumpCount = 0;
    private bool isGround = true;
    [Space(10)]

    [Header("Animation")]
    [SerializeField]
    SpriteRenderer playerSpriteRenderer = null;
    [Space(10)]

    [Header("Camera")]
    [SerializeField]
    private Transform cameraTransform = null;

    private void Awake() 
    {
        playerRigidbody2D = GetComponent<Rigidbody2D>();
        playerSpriteRenderer = GetComponent<SpriteRenderer>();
    }

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetButtonDown("Jump") && jumpCount < maxJumpCount) 
        {
            jumpCount++;
            isGround = false;
            playerRigidbody2D.velocity = new Vector2(
                playerRigidbody2D.velocity.x, 
                jumpForce
                );
        }
        
        if(isGround == true && jumpCount > 0) 
            jumpCount = 0;

        playerRigidbody2D.velocity = new Vector2(
            Input.GetAxis("Horizontal") * maxVelocity, 
            playerRigidbody2D.velocity.y
            );
    }

    private void LateUpdate() 
    {
        if(playerRigidbody2D.velocity.x < 0f)
            playerSpriteRenderer.flipX = true;
        else if (playerRigidbody2D.velocity.x > 0f)
            playerSpriteRenderer.flipX = false;

        if(cameraTransform != null) 
        {
            cameraTransform.position = new Vector3(
                transform.position.x,
                transform.position.y,
                cameraTransform.position.z
                );
        }
    }

    private void FixedUpdate()
    {
        
    }

    private void OnCollisionStay2D(Collision2D collision)
    {
        isGround = Physics2D.OverlapCircle(bottomCollisionPoint.position, .2f, tileLayer);
    }

    private void OnCollisionExit2D(Collision2D collision) 
    {
        isGround = false;
    }
}
