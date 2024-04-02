using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    [Header("Follow Target")]
    [SerializeField]
    private Transform followTransform = null;
    [SerializeField]
    private bool lockY = false;
    [SerializeField]
    private float lockYPosMin = 0f;
    [SerializeField]
    private float lockYPosMax = 0f;
    [Space(10)]

    [Header("Background")]
    [SerializeField]
    private Transform backgroundTransform = null;
    [Space(10)]

    [Header("Middleground")]
    [SerializeField]
    private Transform middlegroundTransform = null;
    [SerializeField]
    [Range(0f, 1f)]
    private float moveScaleFactor = 0.5f;
    [SerializeField]
    private bool verticalParalax = true;
    //[Space(10)]

    private void Awake() 
    {
        if (followTransform == null)
            Debug.LogException(new System.NullReferenceException("Follow Transform is not assigned."));
        if (backgroundTransform == null)
            Debug.LogException(new System.NullReferenceException("Background Transform is not assigned."));
        if (middlegroundTransform == null)
            Debug.LogException(new System.NullReferenceException("Middleground Transform is not assigned."));
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //Camera movement
        transform.position = new Vector3(
            followTransform.position.x,
            lockY == true ? Mathf.Clamp(followTransform.position.y, lockYPosMin, lockYPosMax) : followTransform.position.y,
            transform.position.z
            );

        //Background movement
        backgroundTransform.position = new Vector3(
            transform.position.x,
            transform.position.y,
            backgroundTransform.position.z
            );

        //Middleground movement
        middlegroundTransform.position = new Vector3(
            transform.position.x * moveScaleFactor,
            verticalParalax == true ? transform.position.y * moveScaleFactor : middlegroundTransform.position.y,
            middlegroundTransform.position.z
            );
    }
}
