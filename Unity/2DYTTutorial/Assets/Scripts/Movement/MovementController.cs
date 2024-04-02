using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovementController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField]
    private Rigidbody2D playerRigidbody2D = null;
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
    private int jumpCount = 0;
    private bool isGround = true;
    [Space(10)]

    [Header("Animation")]
    [SerializeField]
    private SpriteRenderer playerSpriteRenderer = null;
    [SerializeField]
    private Animator playerAnimator = null;
    //[Space(10)]

    private void Awake() 
    {
        if (playerRigidbody2D == null)
            Debug.LogException(new System.NullReferenceException("Player Rigidbody 2D not assigned."));
        if (bottomCollisionPoint == null)
            Debug.LogException(new System.NullReferenceException("Bottom Collision Point not assigned."));
        if (playerSpriteRenderer == null)
            Debug.LogException(new System.NullReferenceException("Player Sprite Renderer not assigned."));
        if (playerAnimator == null)
            Debug.LogException(new System.NullReferenceException("Player Animator not assigned."));
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

        playerAnimator.SetFloat("xVelocity", Mathf.Abs(playerRigidbody2D.velocity.x));
        playerAnimator.SetFloat("yVelocity", playerRigidbody2D.velocity.y);
        playerAnimator.SetBool("isGround", isGround);
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
